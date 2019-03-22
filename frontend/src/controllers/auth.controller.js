import * as _ from 'lodash';

import AuthApiService from '../api-services/auth-api-services';

export default class AuthController {
	static setLocalStorageAuthData(data) {
		console.log(data);
		localStorage.setItem('refresh', data.refresh);
		localStorage.setItem('access', data.access);
	}

	static checkLocalStorage() {
		const userData = JSON.parse(localStorage.getItem('user'));

		if (userData) {
			AuthApiService.setAuthHeader();
		}

		return userData;
	}

	static updateUserInLocalStorage(newUserData) {
		const userData = JSON.parse(localStorage.getItem('user'));
		_.assign(userData, newUserData);
		localStorage.setItem('user', JSON.stringify(userData));
	}

	static login(data) {
		return AuthApiService.login(data).then((response) => {
			this.setLocalStorageAuthData(response.data);
			AuthApiService.setAuthHeader();
		});
	}

	static register(data) {
		return AuthApiService.register(data);
	}

	static logout() {
		this.setLocalStorageAuthData({
			token: null,
			user: null,
		});

		AuthApiService.setAuthHeader();
	}

	static changePassword(data) {
		return AuthApiService.changePassword(data);
	}

	static checkAuthStatus() {
		return Boolean(this.checkLocalStorage());
	}
}
