/*jshint esversion: 6 */

import Home from './templates/Home.vue';
import Explore from './templates/Explore.vue';
import Search from './templates/Search.vue';
import TweetList from './templates/TweetList.vue';

import Login from './templates/Login.vue';
import Logout from './templates/Logout.vue';
import Register from './templates/Register.vue';
import Account from './templates/Account.vue';


export const routes = [
    {path: '/', component: Home},
    {path: '/app', component: Explore},
    {path: '/app/explore', component: Explore},
    {path: '/app/search', component: Search},
    {path: '/app/collection:id', component: TweetList},

    {path: '/login', component: Login},
    {path: '/logout', component: Logout},
    {path: '/register', component: Register},
    {path: '/account', component: Account},

];
