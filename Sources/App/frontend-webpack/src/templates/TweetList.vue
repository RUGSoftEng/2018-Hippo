<template lang="html">
    <section class="py-5">
        <div class="container text-center">
            <button type="button" class="btn btn-default" style="margin: 0 100px 20px 100px; width: 400px;" @click="backToCollections">Back to search overview</button>
            <tweet v-for="t in tweetList" :tweetData="t"></tweet>
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
                this.$router.push('/app/search');
            }
        }
    }
</script>

<style lang="css">
</style>
