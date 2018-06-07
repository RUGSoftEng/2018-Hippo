<template>
  <div id="app">
    <nav-bar></nav-bar>
    <div>
      <search-bar></search-bar>
    </div>
  </div>
</template>

<script>
import NavBar from '../components/NavBar.vue';
import SearchBar from '../components/SearchBar.vue';
export default {
  components: {
    'nav-bar': NavBar,
    'search-bar': SearchBar
  }
}
</script>

<style>
  body {
    font-family: 'Lato', 'Helvetica Neue', 'Arial', sans-serif !important;
    position: relative;
    width: 100%;
    color: white !important;
    background: url("../assets/bg-pattern.png"), linear-gradient(to left, #F0F8FF, #C3E4FF);
  }
</style>
