<template lang="html">
  <div class="">
    <home v-if="$route.name == 'H'"></home>
    <login v-if="$route.name == 'L'"></login>
    <app v-if="['TCL', 'TL'].indexOf($route.name) >= 0"></app>
  </div>
</template>

<script>
import App from './templates/App.vue';
import Home from './templates/Home.vue';
import Login from './templates/Login.vue';
export default {
  components: {
    'app': App,
    'home': Home,
    'login': Login
  },
}
</script>

<style lang="css">

</style>
