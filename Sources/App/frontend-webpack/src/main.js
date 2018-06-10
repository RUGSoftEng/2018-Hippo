/*jshint esversion: 6 */
import Vue from 'vue';
import BootstrapVue from "bootstrap-vue";
import Website from './Website.vue';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import axios from 'axios';

import { routes } from './routes';

Vue.use(axios);
Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);

const router = new VueRouter({
    mode: 'history',
    routes
});

new Vue({
    el: '#app',
    router,
    render: h => h(Website)
});