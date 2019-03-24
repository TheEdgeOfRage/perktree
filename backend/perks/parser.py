#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import csv
import re
from .models import Tree, Perk

requirement_pattern = re.compile(r'([\w\s]+) \(([\w\s]+)\)')
ability_pattern = re.compile(r'Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma \d+\+', re.IGNORECASE)
class_pattern = re.compile(r'((Artificer|Barbarian|Bard|Cleric|Druid|Fighter|Monk|Mystic|Paladin|Ranger|Rogue|Sorcerer|Warlock|Wizard|Mage|Alchemist|Magus)(, )?)+', re.IGNORECASE)
race_pattern = re.compile(r'((Dwarf|Elf|Halfling|Human|Dragonborn|Gnome|Half-Elf|Half-Orc|Tiefling)(, )?)+', re.IGNORECASE)


class PerkParser():
	def __init__(self, filename):
		self.filename = filename
		self.trees = None
		self.perks = None

	def parse(self):
		self.strip_whitespaces()
		self.load_csv()
		self.clean_db()
		self.parse_perks()
		self.link_perks()

	def strip_whitespaces(self):
		with open(self.filename, 'r') as file:
			new = [line.rstrip() for line in file]
		with open(self.filename, 'w') as file:
			for line in new:
				file.write(f'{line}\n')

	def load_csv(self):
		with open(self.filename, 'r', newline='') as csvfile:
			perkreader = csv.DictReader(csvfile, delimiter='\t', restkey='requirements')
			self.perks = []
			for row in perkreader:
				self.perks.append(dict(row))

	def clean_db(self):
		Perk.objects.all().delete()
		Tree.objects.all().delete()

	def parse_perks(self):
		for p in self.perks:
			perk = self.create_perk(name=p['name'].strip(), effect=p['effect'].strip(), level=int(p['level']), perk_type=0)
			for tree_name in p['tree'].split(','):
				try:
					tree = Tree.objects.get(name=tree_name)
					perk.trees.add(tree)
				except Tree.DoesNotExist:
					perk.trees.create(name=tree_name)

			p['id'] = Perk.objects.latest('id').id

	def create_perk(self, name, effect='', level=1, perk_type=4, trees=None):
		new_perk = Perk(name=name, effect=effect, level=level, type=perk_type)
		new_perk.save()
		if trees is not None:
			new_perk.trees.add(*trees)

		return new_perk

	def link_perks(self):
		for p in self.perks:
			if 'requirements' not in p:
				continue

			perk = Perk.objects.get(name=p['name'].strip())
			for req_name in p['requirements']:
				req_name = req_name.strip()

				try:
					req = Perk.objects.get(name__iexact=req_name)
					if req.type == 0:
						req_tree = req.trees.all()[0]
					else:
						req_tree = None

				except Perk.DoesNotExist:
					if re.match(class_pattern, req_name):
						req = self.create_perk(name=req_name, level=0, perk_type=1)
					elif re.match(race_pattern, req_name):
						req = self.create_perk(name=req_name, level=0, perk_type=2)
					elif re.match(ability_pattern, req_name):
						req = self.create_perk(name=req_name, level=0, perk_type=3)
					elif 'Skill Focus' in req_name or 'Ability Focus' in req_name:
						req_match = re.match(requirement_pattern, req_name)
						req_tree = Tree.objects.get(name=req_match.group(2))

						req_base_name = req_match.group(1)
						base_req = Perk.objects.get(name=req_base_name)

						req = self.create_perk(name=req_name, effect=base_req.effect, level=base_req.level, perk_type=base_req.type, trees=[req_tree])
					else:
						req = self.create_perk(name=req_name, level=0, perk_type=4)
				perk.parents.add(req)

	def output_transform(self):
		for tree, data in self.trees.items():
			for i in range(len(data['nodes'])):
				perk = data['nodes'][i]
				if 'requirements' in perk:
					perk.pop('requirements')

