<template>
	<v-container>
		<v-layout row wrap id="user-stats">
			<v-flex xl8 offset-xl2 sm12>
				<v-card>
					<center><h1>User stats</h1></center>
					<hr>
					<template v-if="loading">
						<h3>loading</h3>
					</template>
					<template v-else>
						<v-layout row wrap>
							<v-flex lg7 sm12>
								<v-data-table
									:headers="headers"
									:items="maxPerkCounts[fantasy]"
									disable-initial-sort
									hide-actions
									class="elevation-1"
								>
									<template v-slot:items="props">
										<td>{{ props.item.level }}</td>
										<td>{{ props.item.total }}</td>
										<td>{{ props.item.level3 }}</td>
										<td>{{ props.item.level4 }}</td>
									</template>
								</v-data-table>
							</v-flex>
							<v-flex lg2 offset-lg1 sm12>
								<v-layout column id="side-wrapper">
									<v-radio-group v-model="fantasy">
										<v-radio
											label="High fantasy"
											value="high"
										></v-radio>
										<v-radio
											label="Mid fantasy"
											value="mid"
										></v-radio>
										<v-radio
											label="Low fantasy"
											value="low"
										></v-radio>
									</v-radio-group>
									<div>
										<span><b>Level 1: </b>{{ perkCount[1] }}</span><br>
										<span><b>Level 2: </b>{{ perkCount[2] }}</span><br>
										<span><b>Level 3: </b>{{ perkCount[3] }}</span><br>
										<span><b>Level 4: </b>{{ perkCount[4] }}</span><br>
										<span><b>Total: </b>{{ perkCount.total }}</span>
									</div>
								</v-layout>
							</v-flex>
						</v-layout>
					</template>
				</v-card>
			</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
import * as _ from 'lodash';

import UserController from '../controllers/user.controller';

export default {
	name: 'Index',
	components: {
	},
	data () {
		return {
			user: null,
			loading: true,
			fantasy: 'high',
			headers: [
				{ text: 'Character Level', value: 'level', sortable: false },
				{ text: 'Total number of perks', value: 'total', sortable: false },
				{ text: 'Max level 3 perks', value: 'level3', sortable: false },
				{ text: 'Max level 4 perks', value: 'level4', sortable: false },
			],
			maxPerkCounts: {
				high: [
					{ level: 1, total: 2, level3: 0, level4: 0 },
					{ level: 2, total: 4, level3: 1, level4: 1 },
					{ level: 3, total: 6, level3: 2, level4: 1 },
					{ level: 4, total: 8, level3: 3, level4: 1 },
					{ level: 5, total: 10, level3: 3, level4: 2 },
					{ level: 6, total: 12, level3: 4, level4: 2 },
					{ level: 7, total: 14, level3: 5, level4: 2 },
					{ level: 8, total: 16, level3: 6, level4: 3 },
					{ level: 9, total: 18, level3: 7, level4: 3 },
					{ level: 10, total: 20, level3: 8, level4: 3 },
					{ level: 11, total: 22, level3: 8, level4: 4 },
					{ level: 12, total: 24, level3: 9, level4: 4 },
					{ level: 13, total: 26, level3: 10, level4: 4 },
					{ level: 14, total: 28, level3: 11, level4: 5 },
					{ level: 15, total: 30, level3: 12, level4: 5 },
					{ level: 16, total: 32, level3: 13, level4: 5 },
					{ level: 17, total: 34, level3: 14, level4: 6 },
					{ level: 18, total: 36, level3: 15, level4: 6 },
					{ level: 19, total: 38, level3: 16, level4: 6 },
					{ level: 20, total: 40, level3: 17, level4: 7 },
				],
				mid: [
					{ level: 1, total: 1, level3: 0, level4: 0 },
					{ level: 2, total: 3, level3: 1, level4: 0 },
					{ level: 3, total: 4, level3: 1, level4: 0 },
					{ level: 4, total: 5, level3: 2, level4: 1 },
					{ level: 5, total: 7, level3: 2, level4: 1 },
					{ level: 6, total: 8, level3: 3, level4: 1 },
					{ level: 7, total: 9, level3: 3, level4: 1 },
					{ level: 8, total: 11, level3: 4, level4: 2 },
					{ level: 9, total: 12, level3: 4, level4: 2 },
					{ level: 10, total: 13, level3: 5, level4: 2 },
					{ level: 11, total: 15, level3: 5, level4: 2 },
					{ level: 12, total: 16, level3: 6, level4: 3 },
					{ level: 13, total: 17, level3: 6, level4: 3 },
					{ level: 14, total: 19, level3: 7, level4: 3 },
					{ level: 15, total: 20, level3: 7, level4: 3 },
					{ level: 16, total: 21, level3: 8, level4: 4 },
					{ level: 17, total: 23, level3: 8, level4: 4 },
					{ level: 18, total: 24, level3: 9, level4: 4 },
					{ level: 19, total: 25, level3: 9, level4: 4 },
					{ level: 20, total: 27, level3: 10, level4: 5 },
				],
				low: [
				{ level: 1, total: 1, level3: 0, level4: 0 },
				{ level: 2, total: 2, level3: 0, level4: 0 },
				{ level: 3, total: 3, level3: 1, level4: 0 },
				{ level: 4, total: 4, level3: 1, level4: 1 },
				{ level: 5, total: 5, level3: 2, level4: 1 },
				{ level: 6, total: 6, level3: 2, level4: 1 },
				{ level: 7, total: 7, level3: 2, level4: 1 },
				{ level: 8, total: 8, level3: 3, level4: 1 },
				{ level: 9, total: 9, level3: 3, level4: 2 },
				{ level: 10, total: 10, level3: 3, level4: 2 },
				{ level: 11, total: 11, level3: 4, level4: 2 },
				{ level: 12, total: 12, level3: 4, level4: 2 },
				{ level: 13, total: 13, level3: 4, level4: 2 },
				{ level: 14, total: 14, level3: 5, level4: 3 },
				{ level: 15, total: 15, level3: 5, level4: 3 },
				{ level: 16, total: 16, level3: 5, level4: 3 },
				{ level: 17, total: 17, level3: 6, level4: 3 },
				{ level: 18, total: 18, level3: 6, level4: 3 },
				{ level: 19, total: 19, level3: 6, level4: 4 },
				{ level: 20, total: 20, level3: 7, level4: 4 },
				],
			},
		};
	},
	computed: {
		perkCount() {
			const result = {
				0: 0,
				1: 0,
				2: 0,
				3: 0,
				4: 0,
				total: 0,
			};

			if (!this.user) {
				return result;
			}

			_.each(this.user.perks, (perk) => {
				result[perk.level]++;
				if (perk.level > 0) {
					result.total++;
				}
			});

			return result;
		},
	},
	mounted() {
		UserController.getUserPerks().then((response) => {
			this.user = response.data;
			this.loading = false;
		});
	},
};
</script>

<style lang="stylus">
#user-stats
	hr
		margin: 2rem 0

	td
		height 2rem !important

	.v-card
		padding 1rem

	#side-wrapper
		height 100%
		justify-content space-around

		.v-input
			flex unset
</style>
