<template lang="html">
  <div>
    <blockquote class=twitter-tweet>
      <div class="padding-bottom">{{tweetData}}</div>
      <a href="">-By some random guy with 0 followers</a>
    </blockquote>
  </div>
</template>

<script>
export default {
  props: ['tweetData'],

}
</script>

<style scoped lang="css">
blockquote.twitter-tweet {
  display: inline-block;
  font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
  font-size: 12px;
  font-weight: bold;
  line-height: 16px;
  border-color: #00BFFF;
  border-radius: 5px;
  border-style: solid;
  border-width: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
  margin: 10px 5px;
  padding: 0 16px 16px 16px;
  max-width: 468px;
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
</style>
