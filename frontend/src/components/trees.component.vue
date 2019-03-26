<template>
	<v-container grid-list-md text-xs-center class="tree-list">
		<v-layout row wrap>
			<v-flex
				v-for="tree in trees"
				:key="tree.id"
				sm2
				xs6
			>
				<v-btn
					block
					color="secondary"
					@click="openPerks(tree.id)"
				>{{ tree.name }}</v-btn>
			</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
// import * as _ from 'lodash';

import PerkController from '../controllers/perk.controller';

export default {
	name: 'trees',
	components: {
	},
	data () {
		return {
			trees: null,
		};
	},
	methods: {
		openPerks(index) {
			this.$router.push({ name: 'perks', params: { tree: index } });
		},
	},
	mounted() {
		PerkController.getTrees().then((response) => {
			this.trees = response.data;
		});
	},
};
</script>

<style lang="stylus">
@import '../stylus/trees.styl'
</style>

