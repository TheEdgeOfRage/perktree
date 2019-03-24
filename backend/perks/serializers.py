#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from rest_framework import serializers
#  from .models import Perk, Tree


class PerkSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)
	effect = serializers.CharField(read_only=True)
	level = serializers.IntegerField(read_only=True)
	type = serializers.IntegerField(read_only=True)
	#  parents = serializers.ListField(read_only=True)
	#  trees = serializers.ListField(read_only=True)


class TreeSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)

