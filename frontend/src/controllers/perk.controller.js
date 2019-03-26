/*
 * perk.controller.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import PerkApi from '../apis/perk.api';

export default class PerkController {
	static getTrees() {
		return PerkApi.getTrees();
	}

	static getPerks(tree) {
		return PerkApi.getPerks(tree);
	}

	static uploadPerks(file) {
		const data = new FormData();
		data.append('perk_list', file);
		return PerkApi.uploadPerks(data);
	}
}

