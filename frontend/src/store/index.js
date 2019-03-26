/*
 * index.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import Vue from 'vue';
import Vuex from 'vuex';

import perks from './perks';
import auth from './auth';

Vue.use(Vuex);

const storeData = {
  modules: {
    perks,
    auth,
  },
};

export default new Vuex.Store(storeData);


