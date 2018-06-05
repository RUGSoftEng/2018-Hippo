<template>
  <div id="app">
    <nav-bar></nav-bar>
    <div>
      <search-bar></search-bar>
    </div>
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
    font-family: 'Lato', 'Helvetica Neue', 'Arial', sans-serif !important;
    position: relative;
    width: 100%;
    color: white;
    background: url("../src/assets/bg-pattern.png"), linear-gradient(to left, #F0F8FF, #C3E4FF);
  }
</style>
