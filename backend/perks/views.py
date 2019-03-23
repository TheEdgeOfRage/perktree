import json
import os

from os import listdir
from os.path import isfile, join
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


PERKS_DIR = os.environ.get('PERKS_DIR')

if not PERKS_DIR:
	PERKS_DIR = '../static/perks'


def get_tree_list():
	return sorted([file for file in listdir(PERKS_DIR) if isfile(join(PERKS_DIR, file))])


class ListTrees(APIView):
	"""
	View to list all perk trees
	"""
	authentication_classes = (authentication.TokenAuthentication,)
	#  permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, format=None):
		return Response([tree[:-5] for tree in get_tree_list()])

	def post(self, request):
		#  handle_uploaded_file(request.FILES['perk_list'])
		print(request.FILES['perk_list'])
		return Response({'message': 'Upload successful'})


class ListPerks(APIView):
	"""
	View to list all perks in a tree
	"""
	authentication_classes = (authentication.TokenAuthentication,)
	#  permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, tree, format=None):
		print(request.user)
		filename = get_tree_list()[tree]
		with open(f'{PERKS_DIR}/{filename}', 'r') as f:
			return Response(json.load(f))

