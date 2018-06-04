/*jshint esversion: 6 */

import TweetList from './TweetList.vue';
import TweetCollectionList from './TweetCollectionsList.vue';

export const routes = [
  { path: '/', component: TweetCollectionList },
  { path: '/tweetlist', component: TweetList }
];
