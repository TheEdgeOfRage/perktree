<template>
	<v-container class="perktree">
		<v-layout row wrap>
			<v-flex xl8 offset-xl2 sm12>
				<v-card>
					<div id="perktree"></div>
				</v-card>
			</v-flex>
		</v-layout>
		<v-dialog
			v-model="dialog"
			width="500"
		>
			<v-card>
				<v-card-title
					class="headline grey darken-2"
					primary-title
				>
					{{ selectedPerk.name }}
					<v-spacer></v-spacer>
					{{ selectedPerk.level }}
				</v-card-title>
				<v-card-text>{{ selectedPerk.effect }}</v-card-text>
				<v-divider></v-divider>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="error"
						flat
						@click="dialog = false"
					>Close</v-btn>
					<v-btn
						v-if="canUnlock"
						color="primary"
						flat
						@click="unlock()"
					>Unlock</v-btn>
					<v-btn
						v-else-if="canLock"
						color="warning"
						flat
						@click="lock()"
					>Lock</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</v-container>
</template>

<script>
import * as d3 from 'd3';
import Sankey from 'd3.chart.sankey';
import * as _ from 'lodash';

import PerkController from '../controllers/perk.controller';
import UserController from '../controllers/user.controller';

export default {
	name: 'perks',
	components: {
	},
	data () {
		return {
			dialog: false,
			selectedPerk: {
				id: null,
				name: '',
				effect: '',
				level: null,
			},
			user: {
				perks: [],
				base_user: {},
			},
			graphData: {
				nodes: [],
				links: [],
			},
			colorScheme: [
				'#458588',
				'#d79921',
				'#98971a',
				'#cc241d',
				'#d5c4a1',
			],
		};
	},
	computed: {
		canUnlock() {
			const isLocked = _.indexOf(this.user.perks, this.selectedPerk.id);
			if (isLocked !== -1) {
				return false;
			}

			const requirements = _.filter(this.graphData.links, { target: this.selectedPerk });
			const requirement_ids = _.map(requirements, 'source.id');

			return requirement_ids.every((req) => this.user.perks.includes(req));
		},
		canLock() {
			const dependencies = _.filter(this.graphData.links, { source: this.selectedPerk });
			const dependency_ids = _.map(dependencies, 'target.id');
			const isLocked = _.indexOf(this.user.perks, this.selectedPerk.id);
			let hasUnlockedDependencies = false;
			if (dependencies.length !== 0) {
				hasUnlockedDependencies = dependency_ids.every((req) => this.user.perks.includes(req));
			}

			return !hasUnlockedDependencies && isLocked !== -1;
		},
	},
	methods: {
		renderGraph(graphData) {
			const svg = d3.select('#perktree').append('svg');
			const chart = new Sankey.Path(svg);
			const nodes = graphData.nodes;

			chart.nodeWidth(24)
				.nodePadding(6)
				.iterations(32)
				.spread(false)
				.name((n) => {
					return `${n.name} [${n.level}]`;
				})
				.colorNodes((name, node) => {
					return this.colorScheme[node.type];
				})
				.on('node:click', (node) => {
					const clickedNode = _.find(nodes, (n) => {
						return n.name === node.name;
					});
					if (clickedNode.effect) {
						this.selectedPerk = clickedNode;
						this.dialog = true;
					}
				})
				.draw(graphData);
		},
		unlock() {
			if (this.canUnlock) {
				const newPerks = _.clone(this.user.perks);
				newPerks.push(this.selectedPerk.id);
				UserController.updatePerks(newPerks).then((response) => {
					this.user = response.data;
					this.markUnlockedPerks();
					this.dialog = false;
				});
			}
		},
		lock() {
			if (this.canLock) {
				const newPerks = _.difference(this.user.perks, [this.selectedPerk.id]);
				UserController.updatePerks(newPerks).then((response) => {
					this.user = response.data;
					this.markUnlockedPerks();
					this.dialog = false;
				});
			}
		},
		markUnlockedPerks() {
			for (let i = 0; i < this.graphData.nodes.length; i++) {
				const perkId = this.graphData.nodes[i].id;
				const el = this.$el.querySelector(`[data-node-id="${perkId}"] rect`);

				if (_.indexOf(this.user.perks, perkId) !== -1) {
					el.setAttribute('style', `stroke: #d65d0e !important; stroke-width: 3px; fill: ${el.style.fill};`);
				} else {
					el.setAttribute('style', `fill: ${el.style.fill};`);
				}
			}
		},
	},
	mounted() {
		PerkController.getPerks(this.$route.params.tree).then((response) => {
			this.graphData = response.data;
			this.renderGraph(this.graphData);
			UserController.getUser().then((response) => {
				this.user = response.data;
				this.markUnlockedPerks();
			});
		});
	},
};
</script>

<style lang="stylus">
@import '../stylus/perks.styl'
</style>

