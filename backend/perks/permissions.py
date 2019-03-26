#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from rest_framework import permissions


class IsPostOrIsAuthenticated(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method == 'POST':
			return True

		return request.user and request.user.is_authenticated


class IsGetOrIsSuperuser(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method == 'GET':
			return True

		return request.user and request.user.is_superuser and request.user.is_authenticated

