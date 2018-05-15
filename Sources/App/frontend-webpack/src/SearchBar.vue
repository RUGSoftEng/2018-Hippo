<template lang="html">
  <div class="container center">
    <div class="form-inline">
      <input class="form-control mr-sm-3" type="text" v-model="searchText" v-on:keyup.  enter="search(searchText)" placeholder="Search for tweets..." aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" v-on:click="search(searchText)">Search</button>
    </div>
    <tweet-list :tweetList="tweetList"></tweet-list>
  </div>
</template>

<script>
import axios from 'axios';
import TweetList from './TweetList.vue';
export default {
  data() {
    return {
      searchText: '',
      tweetList: [],
      startIndex: 0,
      endIndex: 9,
      newTweetFactor: 10,
    };
  },
  methods:{
    search: function(term) {
      let cmp = this
      axios.get('http://localhost:5000/search/' + term)
        .then(function (response) {
          cmp.tweetList.push.apply(cmp.tweetList, response.data.slice(cmp.startIndex, cmp.endIndex));
          cmp.startIndex += cmp.newTweetFactor;
          cmp.endIndex += cmp.newTweetFactor;
        })
        .catch(function (error) {
          console.log(error);
          cmp.tweetList = [];
       });
    },
    scroll(tweetList){
      let cmp = this
      window.onscroll = ()  => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;

        if (bottomOfWindow) {
          axios.get('http://localhost:5000/search/' + cmp.searchText)
            .then(function (response) {
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
    'tweet-list': TweetList
  },
  watch: {
    searchText: function () {
      this.tweetList = [];
      this.startIndex = 0;
      this.endIndex = 9;
    }
  },
  mounted() {
    this.scroll(this.tweetList);
  }
}
</script>

<style scoped lang="css">
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
  width:293px;
}

.form-control {
  border-radius: 0.5rem
}

.form-control:focus {
  box-shadow: 0 0 0 0.5rem rgba(0, 191, 255, 0.25);
}
</style>
