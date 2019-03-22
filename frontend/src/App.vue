<template>
	<v-app dark>
		<!-- <v-toolbar class="teal darken-2" dark dense fixed clipped-left app> -->
			<!-- <v-toolbar-title> -->
				<!-- <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon> -->
			<!-- </v-toolbar-title> -->

			<!-- <v-spacer></v-spacer> -->

			<!-- <v-toolbar-items class="hidden-xs-only"> -->
				<!-- <template v-if="admin"> -->
				<!-- <v-btn -->
					<!-- v-for="item in toolbarItems['admin']" -->
					<!-- :key="item.text" -->
					<!-- :to="item.path" -->
					<!-- flat -->
				<!-- > -->
					<!-- <v-icon left>{{ item.icon }}</v-icon> -->
					<!-- {{ item.text }} -->
				<!-- </v-btn> -->
				<!-- </template> -->
				<!-- <v-btn -->
				<!-- flat -->
					<!-- v-for="item in toolbarItems[authStatus]" -->
					<!-- :key="item.text" -->
					<!-- :to="item.path" -->
				<!-- > -->
				<!-- <v-icon left>{{ item.icon }}</v-icon> -->
				<!-- {{ item.text }} -->
				<!-- </v-btn> -->
			<!-- </v-toolbar-items> -->
		<!-- </v-toolbar> -->
		<v-content>
			<router-view></router-view>
		</v-content>
	</v-app>
</template>

<script>
export default {
	name: 'App',
};
</script>

<style lang=stylus>
</style>

