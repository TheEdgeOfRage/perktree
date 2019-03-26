#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from os import environ
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .parser import PerkParser
from .models import Perk, Tree, User
from .serializers import PerkSerializer, TreeSerializer, UserSerializer


PERKS_DIR = environ.get('PERKS_DIR')

if not PERKS_DIR:
	PERKS_DIR = '../static/perks'


class TreeView(APIView):
	#  permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, format=None):
		trees = []
		for tree in Tree.objects.all():
			serialized_tree = TreeSerializer(tree)
			trees.append(serialized_tree.data)

		return Response(trees)

	def put(self, request):
		uploaded_file = request.FILES['perk_list']
		with open(uploaded_file.name, 'wb+') as destination:
			for chunk in uploaded_file.chunks():
				destination.write(chunk)

		parser = PerkParser(uploaded_file.name)
		parser.parse()

		return Response({'message': 'Upload successful'})


class PerkView(APIView):
	#  permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, tree_id, format=None):
		output_data = {
			'nodes': [],
			'links': [],
		}

		tree = Tree.objects.get(id=tree_id)
		perks = list(Perk.objects.filter(trees__name__contains=tree.name))
		all_perks = list(perks)
		for i in range(len(perks)):
			perk = all_perks[i]
			for req in perk.parents.all():
				if req not in all_perks:
					all_perks.append(req)
					source_index = len(all_perks) - 1
				else:
					source_index = all_perks.index(req)

				output_data['links'].append({
					'source': source_index,
					'target': i,
					'value': 1,
				})

		for perk in all_perks:
			serialized_perk = PerkSerializer(perk).data
			tree_list = perk.trees.all()
			if tree_list and 'Skill Focus' not in perk.name and 'Ability Focus' not in perk.name and tree not in tree_list:
				serialized_perk['name'] = f'{serialized_perk["name"]} ({tree_list[0].name})'
			output_data['nodes'].append(serialized_perk)

		return Response(output_data)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):
		user = User.objects.get(base_user__id=request.user.id)
		serialized_user = UserSerializer(user).data

		return Response(serialized_user)

	def patch(self, request):
		user = User.objects.get(base_user__id=request.user.id)
		if 'perks' in request.data:
			current_perks = [perk.id for perk in user.perks.all()]
			new_perks = request.data['perks']
			if len(current_perks) < len(new_perks):
				for perk_id in new_perks:
					perk = Perk.objects.get(id=perk_id)
					user.perks.add(perk)
			elif len(current_perks) > len(new_perks):
				removed_perks = list(set(current_perks) ^ set(new_perks))
				for perk_id in removed_perks:
					perk = Perk.objects.get(id=perk_id)
					user.perks.remove(perk)

		serialized_user = UserSerializer(user).data
		return Response(serialized_user)

