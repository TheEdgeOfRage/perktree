<template>
	<v-app dark>
		<v-toolbar color="primary" dense fixed app>
			<v-toolbar-title>
				<router-link :to="{ name: 'index' }">Perktree</router-link>
			</v-toolbar-title>
			<v-spacer></v-spacer>

			<v-toolbar-items>
				<v-btn
					flat
					v-for="item in toolbarItems[authStatus]"
					:key="item.text"
					:to="item.to"
				>
				<v-icon left>{{ item.icon }}</v-icon>
				{{ item.text }}
				</v-btn>
			</v-toolbar-items>
		</v-toolbar>
		<v-content>
			<router-view></router-view>
		</v-content>
	</v-app>
</template>

<script>
import { mapGetters } from 'vuex';

import AuthController from '../controllers/auth.controller.js';

export default {
	name: 'app',
	data() {
		return {
			toolbarItems: {
				true: [
					{ icon: 'fas fa-upload', text: 'Upload perks', to: { name: 'upload-perks' } },
					{ icon: 'fas fa-code-branch', text: 'Perk trees', to: { name: 'trees' } },
					{ icon: 'fas fa-user', text: 'User', to: { name: 'user' } },
					{ icon: 'fas fa-sign-out-alt', text: 'Logout', to: { name: 'logout' } },
				],
				false: [
					{ icon: 'fas fa-code-branch', text: 'Perk trees', to: { name: 'trees' } },
					{ icon: 'fas fa-sign-in-alt', text: 'Login', to: { name: 'login' } },
					{ icon: 'fas fa-user-plus ', text: 'Sign up', to: { name: 'signup' } },
				],
			},
		};
	},
	computed: {
		...mapGetters(['authStatus']),
	},
	mounted() {
		AuthController.refreshToken().catch(() => {
			if (!this.$route.meta.guest) {
				this.$router.push({ name: 'index' });
			}
		});
	},
};
</script>

<style lang="stylus">
@import '../stylus/app.styl'
</style>

