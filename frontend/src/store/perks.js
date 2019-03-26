/*
 * perks.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

const state = {
	perks: [],
};

const getters = {
	perks: (state) => state.perks,
};

const mutations = {
	setPerks(perks) {
		state.perks = perks;
	},
};

export default {
	state,
	getters,
	mutations,
};

