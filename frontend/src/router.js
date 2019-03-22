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
			name: 'signpu',
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
			path: '/admin',
			name: 'admin-panel',
			component: () => import(/* webpackChunkName: "admin" */ './components/auth/admin-panel.component'),
		},
		{
			path: '/perks',
			name: 'perks',
			component: () => import(/* webpackChunkName: "perks" */ './components/perks.component'),
		},
	],
});

router.isCurrentRoute = (routeName) => {
	return router.currentRoute.name === routeName;
};

router.beforeEach((to, from, next) => {
	if (to.meta.guest && AuthController.checkAuthStatus()) {
		return next(to.meta.guest_redirect || '/');
	}

	if (!to.meta.guest && !AuthController.checkAuthStatus()) {
		return next({ name: 'login' });
	}

	if (to.name === 'logout' && AuthController.checkAuthStatus()) {
		AuthController.logout();
		return next({ name: 'login' });
	}

	return next();
});

export default router;
