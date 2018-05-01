<template>
  <div id="app">
    <logo-poster></logo-poster>
    <center>
      <h1 id="tweetTitle">Tweets</h1>
      <search-bar></search-bar>
    </center>
  </div>
</template>

<script>
import LogoPoster from './LogoPoster.vue';
import SearchBar from './SearchBar.vue';
export default {
  components: {
    'logo-poster': LogoPoster,
    'search-bar': SearchBar
  }
}
</script>

<style>
  body {
    background-color: black;
  }
  #tweetTitle {
    color: white;
  }
</style>
