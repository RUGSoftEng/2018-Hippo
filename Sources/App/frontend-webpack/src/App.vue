<template>
  <div id="app">
    <nav-bar></nav-bar>
    <!-- <logo-poster></logo-poster> -->
    <center>
      <h1 id="tweetTitle">Tweets</h1>
      <search-bar></search-bar>
    </center>
  </div>
</template>

<script>
import Navbar from './Navbar.vue';
import LogoPoster from './LogoPoster.vue';
import SearchBar from './SearchBar.vue';
export default {
  components: {
    'nav-bar': Navbar,
    'logo-poster': LogoPoster,
    'search-bar': SearchBar
  }
}
</script>

<style>
  body {
    position: relative;
    width: 100%;
    padding-top: 150px;
    padding-bottom: 100px;
    color: white;
    background: url("../src/assets/bg-pattern.png"), #7b4397;
    background: url("../src/assets/bg-pattern.png"), -webkit-linear-gradient(to left, #7b4397, #dc2430);
    background: url("../src/assets/bg-pattern.png"), linear-gradient(to left, #7b4397, #dc2430);
  }
  #tweetTitle {
    color: white;
  }


</style>
