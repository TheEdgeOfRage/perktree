#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from django.db import models


class Tree(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)


class Perk(models.Model):
	name = models.CharField(max_length=32)
	effect = models.TextField()
	level = models.IntegerField()
	type = models.IntegerField()
	parents = models.ManyToManyField('self', related_name='children', symmetrical=False)
	trees = models.ManyToManyField('Tree', related_name='perks', symmetrical=False)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		ordering = ('name',)
