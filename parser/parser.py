#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import argparse
import csv
import json
import os
import re

PERKS_DIR = os.environ.get('PERKS_DIR')

if not PERKS_DIR:
	PERKS_DIR = 'static/perks'

INPUT_FILE = f'{os.path.abspath(os.path.dirname(__file__))}/perks_all.tsv'

ability_pattern = re.compile(r'Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma \d+\+', re.IGNORECASE)
class_pattern = re.compile(r'((Artificer|Barbarian|Bard|Cleric|Druid|Fighter|Monk|Mystic|Paladin|Ranger|Rogue|Sorcerer|Warlock|Wizard|Mage|Alchemist|Magus)(, )?)+', re.IGNORECASE)
race_pattern = re.compile(r'((Dwarf|Elf|Halfling|Human|Dragonborn|Gnome|Half-Elf|Half-Orc|Tiefling)(, )?)+', re.IGNORECASE)


def strip_whitespaces(filename):
	with open(filename, 'r') as file:
		new = [line.rstrip() for line in file]
	with open(filename, 'w') as file:
		[file.write(f'{line}\n') for line in new]


def load_csv(filename):
	with open(filename, 'r', newline='') as csvfile:
		perkreader = csv.DictReader(csvfile, delimiter='\t', restkey='requirements')
		perks = []
		for row in perkreader:
			perks.append(dict(row))

		return perks


def input_transform(perks):
	trees = {}
	for perk in perks:
		tree = perk['tree'].split('-')[0].strip()
		perk.pop('tree')
		perk['level'] = int(perk['level'])
		perk['colour'] = 0
		perk['name'] = perk['name'].strip()
		perk['effect'] = perk['effect'].strip()
		if 'requirements' in perk:
			for i in range(len(perk['requirements'])):
				perk['requirements'][i] = perk['requirements'][i].strip()

		if tree not in trees:
			trees[tree] = {
				'nodes': [],
				'links': [],
			}

		trees[tree]['nodes'].append(perk)

	return trees


def create_perk(name, effect, level=1, colour=4):
	new_perk = {
		'name': name,
		'effect': effect,
		'level': level,
		'colour': colour,
	}

	return new_perk


def create_links(trees):
	for tree, data in trees.items():
		for i in range(len(data['nodes'])):
			perk = data['nodes'][i]
			if 'requirements' not in perk:
				continue

			for requirement in perk['requirements']:
				found = False
				for j in range(len(data['nodes'])):
					lookup_perk = data['nodes'][j]
					if requirement.startswith(lookup_perk['name']):
						data['links'].append({
							'source': j,
							'target': i,
							'value': 1,
						})
						found = True
						break

				if found:
					continue

				for lookup_tree, lookup_data in trees.items():
					for lookup_perk in lookup_data['nodes']:
						if requirement.startswith(lookup_perk['name']):
							new_perk = create_perk(requirement, lookup_perk['effect'], lookup_perk['level'], lookup_perk['colour'])
							data['nodes'].append(new_perk)
							link_source = len(data['nodes']) - 1

							data['links'].append({
								'source': link_source,
								'target': i,
								'value': 1,
							})
							found = True
							break

					if found:
						break
				else:
					if re.match(class_pattern, requirement):
						new_perk = create_perk(requirement, '', level=0, colour=1)
					elif re.match(race_pattern, requirement):
						new_perk = create_perk(requirement, '', level=0, colour=2)
					elif re.match(ability_pattern, requirement):
						new_perk = create_perk(requirement, '', level=0, colour=3)
					else:
						new_perk = create_perk(requirement, '', level=1, colour=4)

					data['nodes'].append(new_perk)
					data['links'].append({
						'source': len(data['nodes']) - 1,
						'target': i,
						'value': 1,
					})


def output_transform(trees):
	for tree, data in trees.items():
		for i in range(len(data['nodes'])):
			perk = data['nodes'][i]
			if 'requirements' in perk:
				perk.pop('requirements')


def write_json(trees, split):
	os.makedirs(PERKS_DIR, exist_ok=True)
	for tree, data in trees.items():
		with open(f'{PERKS_DIR}/{tree}.json', 'w') as jsonfile:
			json.dump(data, jsonfile)


def main():
	parser = argparse.ArgumentParser(description='Parse tsv perk tree')
	parser.add_argument('input_file', nargs='?', default=INPUT_FILE, help='path to the input file')
	parser.add_argument('-s', '--split', action='store_true', help='split output into multiple json files by tree')
	args = parser.parse_args()

	strip_whitespaces(args.input_file)
	perks = load_csv(args.input_file)
	trees = input_transform(perks)
	create_links(trees)
	#  output_transform(trees)
	write_json(trees, args.split)


if __name__ == '__main__':
	main()

