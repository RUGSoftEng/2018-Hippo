/*jshint esversion: 6 */

import Home from './templates/Home.vue';
import Search from './templates/Search.vue';
import Login from './templates/Login.vue';

export const routes = [
    { path: '/', component: Home},
    { path: '/app', component: Search },
    { path: '/app/explore', component: Search },
    { path: '/app/search', component: Search },
    { path: '/login', component: Login},
];
