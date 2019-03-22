/*
 * perk-tree.helper.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import * as d3 from 'd3';
import * as _ from 'lodash';

const loadGraph = () => {
	d3.json('/static/perks/Dexterity.json', (error, json) => {
		const chart = d3.select('#chart').append('svg').chart('Sankey');
		const color = d3.scale.category10();
		const nodes = json.nodes;

		chart.nodeWidth(20)
			.nodePadding(5)
			.colorNodes((name, node) => {
				return color(node.colour);
			}).on('node:click', (node) => {
				const clicked_node = _.find(nodes, (n) => {
					return n.name === node.name;
				});
				console.log(clicked_node);
			}).draw(json);
	});
};

export default loadGraph;

