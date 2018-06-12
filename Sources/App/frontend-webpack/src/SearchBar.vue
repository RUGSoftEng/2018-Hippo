<template lang="html">
  <div class="container center">
    <div class="search-view form-inline">
      <input class="form-control mr-sm-3 search-box" type="text" v-model="searchText" v-on:keyup.enter="search(searchText)" placeholder="Search for tweets..." aria-label="Search">
    </div>
    <tweet-collections-list v-if="$route.name == 'TCL'" :tweetList="tweetList" :searchTerms="currentlySearchingFor"></tweet-collections-list>
    <tweet-list v-if="$route.name == 'TL'" :tweetList="tweetList"></tweet-list>
  </div>
</template>

<script>
import axios from 'axios';
import TweetCollectionsList from './TweetCollectionsList.vue';
import TweetList from './TweetList.vue';
export default {
  data() {
    return {
      searchText: '',
      tweetList: [],
      startIndex: 0,
      endIndex: 9,
      newTweetFactor: 10,
      currentlySearchingFor: ''
    };
  },
  methods:{
    search: function() {
      this.$router.push('/');
      let cmp = this;
      cmp.currentlySearchingFor = cmp.searchText;
      this.tweetList =   [];
      cmp.startIndex = 0;
      cmp.endIndex = 10;
      axios.get('http://localhost:5000/api/search/' + cmp.searchText, {'timeout': 5000})
        .then(function (response) {
          console.log(response.data)
          cmp.tweetList.push.apply(cmp.tweetList, response.data.slice(cmp.startIndex, cmp.endIndex));
          cmp.startIndex += cmp.newTweetFactor;
          cmp.endIndex += cmp.newTweetFactor;
        })
        .catch(function (error) {
          console.log(error);
       });
    },
    scroll(tweetList){
      let cmp = this
      window.onscroll = ()  => {
        let bottomOfWindow = (document.documentElement.scrollTop + window.innerHeight > document.documentElement.offsetHeight - 0.6 &&
                              document.documentElement.scrollTop + window.innerHeight < document.documentElement.offsetHeight + 0.6);
        console.log(document.documentElement.scrollTop + window.innerHeight, document.documentElement.offsetHeight);
        if (bottomOfWindow) {
          axios.get('http://localhost:5000/api/search/' + cmp.currentlySearchingFor, {'timeout': 5000})
            .then(function (response) {
              console.log("Trying to scroll");
              cmp.tweetList.push.apply(cmp.tweetList, response.data.slice(cmp.startIndex, cmp.endIndex));
              cmp.startIndex += cmp.newTweetFactor;
              cmp.endIndex += cmp.newTweetFactor;
            })
            .catch(function (error) {
              console.log(error);
              cmp.tweetList = [];
           });
        }
      }
    }
  },
  components: {
    'tweet-collections-list': TweetCollectionsList,
    'tweet-list': TweetList
  },
  mounted() {
    this.scroll(this.tweetList);
  }
}
</script>

<style scoped lang="css">
  .search-box
  {
    border: #D1D1D1 solid 0.1em;
    padding-left: 2.75em;
    width: 30em !important;
    background-image: url("../src/assets/icons8-search.svg");
    background-repeat: no-repeat;
    background-position: 0.8em 0.35em;
    background-size: 1.5em;
  }

  .search-view
  {
      padding-top: 100px;
      padding-bottom: 100px;
  }

.btn {
  border-color: #00BFFF /*rgb(255, 125, 125)*/ !important;
  background-color: inherit !important;
  border-radius: 0.5rem
}

.btn:hover, .btn:visited {
  box-shadow: 0 0 0 0.5rem rgba(0, 191, 255, 0.25) !important;
}

.btn:active {
  background-color: #00BFFF !important;
}

.btn:focus {
  box-shadow: 0 0 0 0.5rem rgba(255, 125, 125,0.25) !important;
}

.btn-outline-success {
  color: #00BFFF !important;
}

.btn-outline-success:active {
  color: rgb(255, 255, 255) !important;
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
