/*
 * router.js
 * Copyright (C) 2019 pavle <pavle.portic@tilda.center>
 *
 * Distributed under terms of the BSD-3-Clause license.
 */

import Vue from 'vue';
import Router from 'vue-router';

import Index from './components/index.component';
import Login from './components/auth/login.component';
import Signup from './components/auth/signup.component';

import AuthController from './controllers/auth.controller';

Vue.use(Router);

const router = new Router({
	mode: 'history',
	routes: [
		{
			path: '/',
			name: 'index',
			component: Index,
			meta: {
				guest: true,
			},
		},
		{
			path: '/login',
			name: 'login',
			component: Login,
			meta: {
				guest: true,
			},
		},
		{
			path: '/signup',
			name: 'signup',
			component: Signup,
			meta: {
				guest: true,
			},
		},
		{
			path: '/logout',
			name: 'logout',
		},
		{
			path: '/upload',
			name: 'upload-perks',
			component: () => import(/* webpackChunkName: "perks" */ './components/upload-perks.component'),
		},
		{
			path: '/trees',
			name: 'trees',
			component: () => import(/* webpackChunkName: "perks" */ './components/trees.component'),
			meta: {
				guest: true,
			},
		},
		{
			path: '/perks/:tree',
			name: 'perks',
			component: () => import(/* webpackChunkName: "perks" */ './components/perks.component'),
			meta: {
				guest: true,
			},
		},
		{
			path: '/user',
			name: 'user',
			component: () => import(/* webpackChunkName: "user" */ './components/user.component'),
		},
	],
});

router.isCurrentRoute = (routeName) => {
	return router.currentRoute.name === routeName;
};

router.beforeEach((to, from, next) => {
	if (to.name === 'logout') {
		AuthController.logout();
		return next({ name: 'index' });
	}

	if (!to.meta.guest && !AuthController.getAuthStatus()) {
		return next({ name: 'login' });
	}

	return next();
});

export default router;
