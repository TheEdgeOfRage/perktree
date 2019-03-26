#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from django.db import models
from django.contrib.auth.models import User as AuthUser


class Tree(models.Model):
	name = models.CharField(max_length=64, unique=True)

	def __str__(self):
		return self.name

	def __repr__(self):
		return f'<Tree: {str(self)}>'

	class Meta:
		ordering = ('name',)


class Perk(models.Model):
	name = models.CharField(max_length=64)
	effect = models.TextField()
	level = models.IntegerField()
	type = models.IntegerField()
	parents = models.ManyToManyField('self', related_name='children', symmetrical=False)
	trees = models.ManyToManyField('Tree', related_name='perks', symmetrical=False)

	def __str__(self):
		return f'{self.name} [{self.level}]'

	def __repr__(self):
		return f'<Perk: {str(self)}>'

	class Meta:
		ordering = ('name',)


class User(models.Model):
	base_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
	perks = models.ManyToManyField(Perk, related_name='users', symmetrical=False)

	def __str__(self):
		return f'{self.base_user.username} ({self.id})'

	def __repr__(self):
		return f'<User: {str(self)}>'

