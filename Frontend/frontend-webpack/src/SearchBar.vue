<template lang="html">
  <div class="container center">
    <div class="form-inline">
      <input class="form-control mr-sm-3" type="text" v-model="searchText" placeholder="Search for tweets..." aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" v-on:click="search(searchText)">Search</button>
    </div>
    <tweet-list :tweetList="tweetList"></tweet-list>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      searchText: '',
      tweetList: []
    };
  },
  methods:{
    search: function(term) {
      // this.$data.tweetList = [{'tweet-id': "ABC", 'content': "Hello world!", 'keywords': ["hello","world"]},
      //        {'tweet-id': "BBC", 'content': "Hello earth!", 'keywords': ["hello","earth"]},
      //        {'tweet-id': "CBC", 'content': "These tweets are placeholders because there is no backend yet as of this pull request!", 'keywords': ["hello","universe"]}];
      let componentContext = this;
      axios.get('http://localhost:5000/search/' + term)
        .then(function (response) {
          componentContext.$data.tweetList = response.data;
        })
        .catch(function (error) {
          console.log(error);
       });
    }
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
