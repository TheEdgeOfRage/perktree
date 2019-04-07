/*
 * user.api.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import Axios from 'axios';

const ENDPOINTS = {
	USER: '/user',
};

export default class AuthApi {
	static getUser() {
		return Axios.get(ENDPOINTS.USER);
	}

	static getUserPerks() {
		return Axios.get(ENDPOINTS.USER, { params: { full: 1 } });
	}

	static createUser(data) {
		return Axios.post(ENDPOINTS.USER, data);
	}

	static updatePerks(data) {
		return Axios.patch(ENDPOINTS.USER, data);
	}
}

