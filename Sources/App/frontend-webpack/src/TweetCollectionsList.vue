<template lang="html">
  <section class="py-5">
    <div class="container text-center">
      <tweetCollection v-for="t in tweetList" :tweetData="t.content"></tweetCollection>
    </div>
  </section>
</template>

<script>
import TweetCollection from './TweetCollection.vue';
export default {
  props: ['tweetList'],
  data: {
    tweet: "yes"
  },
  components: {
    'tweetCollection': TweetCollection
  }
}
</script>

<style lang="css">
</style>
