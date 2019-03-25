<template>
	<v-layout>
		<v-flex md12 lg6 offset-lg3>
			<v-card class="admin-form-card">
				<upload-button
					:fileChangedCallback="upload"
					:title="buttonText"
				>
					<template
						v-if="loading"
						slot="icon-left"
					>
						<v-icon left>fas fa-spinner</v-icon>
					</template>
					<template
						v-else
						slot="icon-left"
					>
						<v-icon left>fas fa-upload</v-icon>
					</template>
				</upload-button>
			</v-card>
		</v-flex>
		<v-dialog
			v-model="dialog"
			width="500"
		>
			<v-card>
				<v-card-title
					class="headline grey darken-2"
					error-title
				>Error while uploading</v-card-title>
				<v-card-text>{{ error }}</v-card-text>
				<v-divider></v-divider>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="primary"
						flat
						@click="dialog = false"
					>Close</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</v-layout>
</template>

<script>
import UploadButton from 'vuetify-upload-button';

import PerksController from '../controllers/perks.controller';

export default {
	name: 'admin-panel',
	components: {
		UploadButton,
	},
	data() {
		return {
			loading: false,
			error: '',
			dialog: false,
		};
	},
	computed: {
		buttonText() {
			return this.loading ? 'Loading...' : 'Upload';
		},
	},
	methods: {
		upload(file) {
			this.loading = true;
			PerksController.uploadPerks(file).then(() => {
				this.loading = false;
				this.$router.push({ name: 'trees' });
			}).catch((error) => {
				this.error = error.response.data;
				this.dialog = true;
				this.loading = false;
			});
		},
	},
};
</script>

<style lang="stylus">
.admin-form-card
	margin-top 5rem
	padding 2rem
</style>

