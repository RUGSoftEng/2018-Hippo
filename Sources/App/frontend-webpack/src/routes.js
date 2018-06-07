/*jshint esversion: 6 */

import TweetList from './TweetList.vue';
import TweetCollectionList from './TweetCollectionsList.vue';
import Home from './Home.vue';
import Login from './Login.vue';
export const routes = [
  { path: '/app', name:'TCL', component: TweetCollectionList },
  { path: '/', name: 'H', component: Home},
  { path: '/login', name: 'L', component: Login},
  { path: '/app/tweetlist:id', name: 'TL', component: TweetList },

];
