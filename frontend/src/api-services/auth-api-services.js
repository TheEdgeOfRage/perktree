import Axios from 'axios';

const ENDPOINTS = {
	LOGIN: '/token/',
	REFRESH: '/token/refresh/',
	USER: '/user/',
};
const AUTH_HEADER = 'Authorization';

export default class AuthApiService {
	static setAuthHeader() {
		Axios.defaults.headers.common[AUTH_HEADER] = `Bearer ${localStorage.getItem('access_token')}`;
	}

	static login(data) {
		return Axios.post(ENDPOINTS.LOGIN, data);
	}

	static signup(data) {
		return Axios.post(ENDPOINTS.USER, data);
	}

	static changePassword(data) {
		return Axios.patch(ENDPOINTS.USER, data);
	}
}

