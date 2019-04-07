#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from django.contrib.auth.models import User as AuthUser
from rest_framework import serializers

from .models import Perk, Tree, User


class PerkSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)
	effect = serializers.CharField(read_only=True)
	level = serializers.IntegerField(read_only=True)
	type = serializers.IntegerField(read_only=True)

	class Meta:
		model = Perk
		fields = ('id', 'name', 'effect', 'level', 'type')


class TreeSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)

	class Meta:
		model = Tree
		fields = ('id', 'name')


class AuthUserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(read_only=True)
	email = serializers.CharField(read_only=True)

	class Meta:
		model = AuthUser
		fields = ('id', 'username', 'email')


class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	perks = serializers.PrimaryKeyRelatedField(queryset=Perk.objects.all(), many=True)
	base_user = AuthUserSerializer(required=False, many=False)

	class Meta:
		model = User
		fields = ('id', 'perks', 'base_user')


class UserPerksSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	perks = PerkSerializer(read_only=True, many=True)

	class Meta:
		model = User
		fields = ('id', 'perks')

