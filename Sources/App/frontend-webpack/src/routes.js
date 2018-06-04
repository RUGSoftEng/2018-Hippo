/*jshint esversion: 6 */

import TweetList from './TweetList.vue';
import TweetCollectionList from './TweetCollectionsList.vue';

export const routes = [
  { path: '/', name:'TCL', component: TweetCollectionList },
  { path: '/tweetlist', name:'TL', component: TweetList }
];
