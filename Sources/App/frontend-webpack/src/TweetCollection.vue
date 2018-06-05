<template lang="html">
  <div>
   <blockquote class=tweet-collection>
     <h1 class="category">{{searchTerms}}</h1>
     <div class="line"></div>
     <div class="padding-bottom">{{tweetData}}</div>
     <div>
       <i style="color: #1dcaff; font-size: 30px; text-align: left; float: left;" class="fa fa-twitter"></i>
       <h5 style="text-align: left; float: left">420</h5>
       <i style="color: red; font-size: 30px; text-align: left; float: left; padding-left: 5px;" class="fa fa-heart"></i>
       <h5 style="text-align: left; float: left; padding-left: 5px">420</h5>
       <button class="collection-button" style="text-align: right; float: right; background: #1569C7; color: white; border: none; border-radius: 4px;" v-on:click="switchToTweets()">More</button>

     </div>
   </blockquote>
 </div>
</template>

<script>
export default {
  props: ['tweetData', 'searchTerms', 'categoryNum'],
  methods: {
    switchToTweets: function() {
      console.log("Switching to tweets...");
      window.scrollBy(0, -1000);
      this.$router.push({name: 'TL', params: {id: this.categoryNum}});
    }
  }
}
</script>

<style scoped lang="css">
    .collection-button {
        border-color: #00BFFF /*rgb(255, 125, 125)*/ !important;
        background-color: inherit !important;
        border-radius: 0.5rem
    }

    .collection-button:hover, .collection-button:visited {
        box-shadow: 0 0 0 0.5rem rgba(0, 191, 255, 0.25) !important;
    }

    .collection-button:active {
        background-color: #00BFFF !important;
    }

    .collection-button:focus {
        box-shadow: 0 0 0 0.5rem rgba(255, 125, 125,0.25) !important;
    }

    blockquote.tweet-collection {
        display: inline-block;
        color: black;
        font-size: 20px;
        line-height: 24px;
        border-radius: 10px;
        border: 5px solid #00BFFF;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
        margin: 10px 5px;
        padding: 16px 16px 16px 16px;
        width: 700px;
        background-color: white;
    }

    blockquote.tweet-collection p {
        font-size: 16px;
        font-weight: normal;
        line-height: 20px;
    }

    blockquote.tweet-collection a {
        color: inherit;
        font-weight: normal;
        text-decoration: none;
        outline: 0 none;
    }

    blockquote.tweet-collection a:hover,
    blockquote.tweet-collection a:focus {
        text-decoration: underline;
    }

    .category {
        padding: 0 0 0 60px;
        font-size: 38px;
    }

    .line {
        width: 660px;
        margin-right: 20px;
        border-bottom: 2px solid black;
        position: absolute;
    }
</style>
