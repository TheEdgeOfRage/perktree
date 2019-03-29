<template>
	<v-container>
	</v-container>
</template>

<script>

export default {
	name: 'Index',
	components: {
	},
	data () {
		return {
		};
	},
	methods: {
	},
	mounted() {
		this.$router.push({ name: 'trees' });
	},
};
</script>

