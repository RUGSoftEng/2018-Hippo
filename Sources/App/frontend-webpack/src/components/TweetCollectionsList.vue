<template lang="html">
    <section class="py-5">
        <div class="container text-center">
            <tweetCollection v-for="(c, i) in categoryList" v-if="c.tweets.length > 0" :tweetData="c.tweets[0].content"
                             :searchTerms="getKeywords(c.keywords)" :categoryNum="i"></tweetCollection>
        </div>
    </section>
</template>

<script>
    import TweetCollection from './TweetCollection.vue';

    export default {
        props: ['categoryList', "searchTerms"],
        components: {
            'tweetCollection': TweetCollection
        },
        methods: {
            getKeywords(list) {
                let string = "";
                for (let i = 0; i < list.length - 1; i++) {
                    string = string + (list[i] + ", ");
                }
                string += list[list.length - 1];
                return string;
            }

        }
    }
</script>

<style lang="css">
</style>
