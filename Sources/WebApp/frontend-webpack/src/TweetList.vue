<template lang="html">
  <section class="py-5">
    <div class="container text-center">
      <tweet v-for="t in tweetList" :tweetData="t.content"></tweet>
    </div>
  </section>
</template>

<script>
import Tweet from './Tweet.vue';
export default {
  props: ['tweetList'],
  components: {
    'tweet': Tweet
  }
}
</script>

<style lang="css">
</style>
