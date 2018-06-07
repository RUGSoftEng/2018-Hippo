/*jshint esversion: 6 */

import TweetList from './components/TweetList.vue';
import TweetCollectionList from './components/TweetCollectionsList.vue';
import Home from './templates/Home.vue';
import Login from './templates/Login.vue';
export const routes = [
  { path: '/app', name:'TCL', component: TweetCollectionList },
  { path: '/', name: 'H', component: Home},
  { path: '/login', name: 'L', component: Login},
  { path: '/app/tweetlist:id', name: 'TL', component: TweetList },

];
