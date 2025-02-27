import Axios from 'axios';
import Vue from 'vue';
import Raven from 'raven-js';
import RavenVue from 'raven-js/plugins/vue';


import './plugins/vuetify';

import App from './components/app.vue';
import { config } from './config';
import router from './router';
import store from './store/';
import AuthController from './controllers/auth.controller';

import 'roboto-fontface/css/roboto/roboto-fontface.css';
import 'material-design-icons-iconfont/dist/material-design-icons.css';

Vue.config.productionTip = false;

const configureHttp = () => {
	Axios.defaults.baseURL = config.getApiUrl();
	Axios.defaults.headers.Accept = 'application/json';
	// Axios.defaults.headers['Access-Control-Allow-Origin'] = '*';
	Axios.interceptors.response.use(
		(response) => {
			return response;
		},
		(error) => {
			if (error.response && error.response.status === 401) {
				AuthController.refreshToken().catch(() => {
					router.push({
						name: 'logout',
					});
				});
			}

			return Promise.reject(error);
		}
	);
};

const configureRaven = () => {
	if (config.getEnv() !== 'dev') {
		Raven
			.config('https://2b1b0eea285244289175e53d65421fac@sentry.theedgeofrage.com/3')
			.addPlugin(RavenVue, Vue)
			.install();
	}
};

configureHttp();
configureRaven();
AuthController.setupToken();

new Vue({
	router,
	store,
	render (h) {
		return h(App);
	},
}).$mount('#app');

