/*jshint esversion: 6 */

import TweetList from './TweetList.vue';
import TweetCollectionList from './TweetCollectionsList.vue';
import Home from './Home.vue';
export const routes = [
  { path: '/', name:'TCL', component: TweetCollectionList },
  { path: '/home', name: 'H', component: Home},
  { path: '/tweetlist:id', name: 'TL', component: TweetList }
];
