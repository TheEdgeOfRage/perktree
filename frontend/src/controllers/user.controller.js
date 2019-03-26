/*
 * user.controller.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import UserApi from '../apis/user.api';

export default class AuthController {
	static getUser() {
		return UserApi.getUser();
	}

	static updatePerks(perks) {
		const data = {
			perks,
		};

		return UserApi.updatePerks(data);
	}
}

