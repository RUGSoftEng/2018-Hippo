/*jshint esversion: 6 */
import Vue from 'vue';
import BootstrapVue from "bootstrap-vue";
import Website from './Website.vue';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import VueRouter from 'vue-router';
import { routes } from './routes';

Vue.use(BootstrapVue);
Vue.use(VueRouter);

const router = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(Website)
});
