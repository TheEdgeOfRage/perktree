#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import json

from os import listdir, environ
from os.path import isfile, join
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication  # , permissions

from .parser import PerkParser
from .models import Perk, Tree
from .serializers import PerkSerializer, TreeSerializer


PERKS_DIR = environ.get('PERKS_DIR')

if not PERKS_DIR:
	PERKS_DIR = '../static/perks'


class Trees(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
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


class Perks(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
	#  permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, tree_id, format=None):
		output_data = {
			'nodes': [],
			'links': [],
		}

		#  link ={
			#  'source': link_source,
			#  'target': i,
			#  'value': 1,
		#  }

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
			serialized_perk = PerkSerializer(perk)
			output_data['nodes'].append(serialized_perk.data)

		return Response(output_data)

