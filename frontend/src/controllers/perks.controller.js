/*
 * perks.controller.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import PerkApi from '../apis/perk.api';
// import router from '../router';

export default class PerksController {
	static getTrees() {
		return PerkApi.getTrees();
	}

	static getPerks(tree) {
		return PerkApi.getPerks(tree);
	}
}
