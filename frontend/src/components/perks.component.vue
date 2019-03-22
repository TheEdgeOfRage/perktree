<template>
	<v-content>
		<div id="stuff"></div>
	</v-content>
</template>

<script>
import Graph from '../helpers/perk-tree.helper.js';

export default {
	name: 'Perks',
	components: {
	},
	data () {
		return {
		};
	},
	methods: {
	},
	mounted() {
		const g = new Graph();
		console.log(g);
	},
};
</script>

