<template lang="html">
    <div class="container center">
        <div class="search-view form-inline">
            <input class="form-control mr-sm-3 search-box" type="text" v-model="searchText"
                   v-on:keyup.enter="search(searchText)" placeholder="Search for ideas..." aria-label="Search" autofocus>
        </div>
        <tweet-collections-list v-if="$route.path == '/app/search'" :categoryList="categories"
                                :searchTerms="currentlySearchingFor"></tweet-collections-list>
        <tweet-list v-else :tweetList="currentTweetsDisplayed"></tweet-list>
    </div>
</template>

<script>
    import axios from 'axios';
    import TweetCollectionsList from './TweetCollectionsList.vue';
    import TweetList from '../templates/TweetList.vue';

    export default {
        data() {
            return {
                searchText: '',
                tweetList: [],
                currentTweetsDisplayed: [],
                startIndex: 0,
                endIndex: 10,
                newTweetFactor: 10,
                currentlySearchingFor: '',

                categories: []
            };
        },
        methods: {
            search: function () {
                this.categories = [];
                this.$router.push('/app/search');
                let cmp = this;
                cmp.currentlySearchingFor = cmp.searchText;
                this.tweetList = [];
                cmp.startIndex = 0;
                cmp.endIndex = 10;

                axios.get('http://localhost:5000/api/search_category/' + cmp.searchText, {
                    auth: {
                        username: email,
                        password: password
                    },
                })
                    .then(function (response) {
                        console.log(response.data);

                        cmp.categories = response.data;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },

            displayTweets() {
                let cmp = this
                console.log("Displayig Tweets");
                console.log(cmp.tweetList);
                cmp.currentTweetsDisplayed.push.apply(cmp.currentTweetsDisplayed, cmp.tweetList.slice(cmp.startIndex, cmp.endIndex));
                cmp.startIndex += cmp.newTweetFactor;
                cmp.endIndex += cmp.newTweetFactor;
                window.onscroll = () => {
                    let bottomOfWindow = (document.documentElement.scrollTop + window.innerHeight > document.documentElement.offsetHeight - 0.6 &&
                        document.documentElement.scrollTop + window.innerHeight < document.documentElement.offsetHeight + 0.6);
                    console.log(document.documentElement.scrollTop + window.innerHeight, document.documentElement.offsetHeight);
                    if (bottomOfWindow) {
                        //  axios.get('http://localhost:5000/api/search/' + cmp.currentlySearchingFor, {'timeout': 5000})
                        //  .then(function (response) {
                        console.log("Trying to scroll");
                        cmp.currentTweetsDisplayed.push.apply(cmp.currentTweetsDisplayed, cmp.tweetList.slice(cmp.startIndex, cmp.endIndex));
                        cmp.startIndex += cmp.newTweetFactor;
                        cmp.endIndex += cmp.newTweetFactor;
                        //  })
                        //  .catch(function (error) {
                        //    console.log(error);
                        //    cmp.tweetList = [];
                        // });
                    }
                }
            }
        },
        components: {
            'tweet-collections-list': TweetCollectionsList,
            'tweet-list': TweetList
        },
        watch: {
            $route(to, from) {
                console.log("Changed route");
                console.log(to, from);
                console.log(to.params.id);
                if (to.params.id != undefined) {
                    this.tweetList = this.categories[to.params.id].tweets;
                    this.displayTweets();
                } else {
                    this.tweetList = [];
                    this.currentTweetsDisplayed = [];
                    this.startIndex = 0;
                    this.endIndex = 10;
                    window.onscroll = () => {
                    };
                }
            }
        }
        //mounted() {
        //  this.displayTweets();
        //}
    }
</script>

<style scoped lang="css">
    .search-box {
        border: #D1D1D1 solid 0.1em;
        padding-left: 2.75em;
        width: 30em !important;
        background: white url("../assets/icons8-search.svg") no-repeat 0.8em 0.4em;
        background-size: 1.25em;
        font-size: 1.4em;
        border-radius: 2.5em;
    }

    .search-view {
        padding-top: 100px;
        padding-bottom: 100px;
    }

    .form-inline {
        margin: 0 auto;
        width: 30em;
    }

    .form-control {
        border-radius: 0.5rem
    }

    .form-control:focus {
        box-shadow: 0 0 5px rgb(209, 209, 209);
    }
</style>
