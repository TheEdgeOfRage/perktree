<template>
	<v-layout>
		<v-flex md12 lg6 offset-lg3 >
			<v-card class="signup-form-card">
				<h3>Sign up</h3>
				<form @submit="submit">
					<v-text-field
						v-model="username"
						label="Username"
						type="text"
						required>
					</v-text-field>
					<v-text-field
						v-model="email"
						label="Email"
						type="email"
						required>
					</v-text-field>
					<v-text-field
						v-model="password"
						label="Password"
						type="password"
						required>
					</v-text-field>
					<v-text-field
						v-model="passwordConfirm"
						label="Confirm password"
						type="password"
						required>
					</v-text-field>
					<p v-for="(error, index) in signupErrors"
						:key="index"
						class="signup-errors">
						{{ error }}
					</p>

					<v-btn type="submit">Signup</v-btn>
				</form>
			</v-card>
		</v-flex>
	</v-layout>
</template>

<script>
	import UserController from '../../controllers/user.controller';

	export default {
		name: 'signup',
		data() {
			return {
				username: '',
				email: '',
				password: '',
				passwordConfirm: '',
				signupErrors: [],
			};
		},
		methods: {
			submit(event) {
				event.preventDefault();
				this.signupErrors = [];

				if (this.password !== this.passwordConfirm) {
					this.signupErrors.push('Passwords do not match');
					return;
				}

				const data = {
					username: this.username,
					email: this.email,
					password: this.password,
				};
				UserController.createUser(data).then(() => {
					this.$router.push({ name: 'index' });
				}).catch((error) => {
					if (error.response) {
						this.signupErrors.push(error.response.data);
					}
				});
			},
		},
	};
</script>

<style lang="stylus">
.signup-form-card
	padding 2rem
	margin-top 5rem

.signup-errors
	color red
</style>

