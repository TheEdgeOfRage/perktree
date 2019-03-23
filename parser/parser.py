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
	PERKS_DIR = '../static/perks'

INPUT_FILE = f'{os.path.abspath(os.path.dirname(__file__))}/perks_all.tsv'

ability_pattern = re.compile(r'Strength|Dexterity|Constitution|Intelligence|Wisdom|Charisma \d+\+', re.IGNORECASE)
class_pattern = re.compile(r'((Artificer|Barbarian|Bard|Cleric|Druid|Fighter|Monk|Mystic|Paladin|Ranger|Rogue|Sorcerer|Warlock|Wizard|Mage|Alchemist|Magus)(, )?)+', re.IGNORECASE)
race_pattern = re.compile(r'((Dwarf|Elf|Halfling|Human|Dragonborn|Gnome|Half-Elf|Half-Orc|Tiefling)(, )?)+', re.IGNORECASE)


def load_csv(filename):
	with open(filename, newline='') as csvfile:
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
		if tree not in trees:
			trees[tree] = {
				'nodes': [],
				'links': [],
			}

		trees[tree]['nodes'].append(perk)

	return trees


def create_perk(name, effect, level=1, colour=4):
	return {
		'name': name,
		'effect': effect,
		'level': level,
		'colour': colour,
	}


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
					if lookup_perk['name'] in requirement:
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
						if lookup_perk['name'] in requirement:
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

	perks = load_csv(args.input_file)
	trees = input_transform(perks)
	create_links(trees)
	#  output_transform(trees)
	write_json(trees, args.split)


if __name__ == '__main__':
	main()

