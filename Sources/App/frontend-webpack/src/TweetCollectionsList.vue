<template lang="html">
  <section class="py-5">
    <div class="container text-center">
      <tweetCollection v-if="tweetList.length > 0" :tweetData="tweetList[0].content" :searchTerms="searchTerms"></tweetCollection>
    </div>
  </section>
</template>

<script>
import TweetCollection from './TweetCollection.vue';
export default {
  props: ['tweetList', "searchTerms"],
  components: {
    'tweetCollection': TweetCollection
  }
}
</script>

<style lang="css">
</style>
