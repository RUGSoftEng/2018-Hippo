<template lang="html">
  <div>
   <blockquote class=twitter-tweet>
     <h1 class="category">{{searchTerms}}</h1>
     <div class="line"></div>
     <div class="padding-bottom">{{tweetData}}</div>
     <div>
       <i style="color: #1dcaff; font-size: 30px; text-align: left; float: left;" class="fa fa-twitter"></i>
       <h5 style="text-align: left; float: left">420</h5>
       <i style="color: red; font-size: 30px; text-align: left; float: left; padding-left: 5px;" class="fa fa-heart"></i>
       <h5 style="text-align: left; float: left; padding-left: 5px">420</h5>
       <button style="text-align: right; float: right; background: #1569C7; color: white; border: none; border-radius: 4px;" v-on:click="switchToTweets()">More</button>

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
blockquote.twitter-tweet {
  display: inline-block;
  font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
  color: black;
  font-size: 20px;
  line-height: 24px;
  border-color: #00BFFF;
  border-radius: 10px;
  border-style: solid;
  border-width: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
  margin: 10px 5px;
  padding: 16px 16px 16px 16px;
  width: 700px;
  background-color: white;
}

blockquote.twitter-tweet p {
  font-size: 16px;
  font-weight: normal;
  line-height: 20px;
}

blockquote.twitter-tweet a {
  color: inherit;
  font-weight: normal;
  text-decoration: none;
  outline: 0 none;
}

blockquote.twitter-tweet a:hover,
blockquote.twitter-tweet a:focus {
  text-decoration: underline;
}

.padding-bottom {
  padding-bottom: 1rem
}

@import url(https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900);

.category {
 padding: 0px 0px 0px 60px;
 font-size: 38px;
}

.line{
width: 660px;
margin-right: 20px;
border-bottom: 2px solid black;
position: absolute;
}
</style>
