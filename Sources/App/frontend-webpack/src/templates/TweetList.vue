<template lang="html">
  <section class="py-5">
    <div class="container text-center">
      <button type="button" class="btn btn-default" @click="backToCollections">Back to search overview</button>
      <tweet v-for="t in tweetList" :tweetData="t.content"></tweet>
    </div>
  </section>
</template>

<script>
import Tweet from '../components/Tweet.vue';
export default {
  props: ['tweetList'],
  components: {
    'tweet': Tweet
  },
  methods: {
    backToCollections() {
      this.$router.push('/app');
    }
  }
}
</script>

<style lang="css">
</style>
