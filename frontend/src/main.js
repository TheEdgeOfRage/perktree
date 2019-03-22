import Axios from 'axios';
import Vue from 'vue';
import './plugins/vuetify';

import App from './App.vue';
import { config } from './config';
import router from './router';

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
        router.push({
          name: 'logout',
        });
      }

      return Promise.reject(error);
    }
  );
};

configureHttp();

new Vue({
  router,
  render (h) {
    return h(App);
  },
}).$mount('#app');

