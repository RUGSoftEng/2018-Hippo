<template lang="html">
  <div class="">
    <home v-if="$route.name == 'H'"></home>
    <app v-if="['TCL', 'TL'].indexOf($route.name) >= 0"></app>
  </div>
</template>

<script>
import App from './App.vue';
import Home from './Home.vue';
export default {
  components: {
    'app': App,
    'home': Home
  },  
  beforeCreate() {
    this.$router.push('/home');
  }
}
</script>

<style lang="css">
</style>
