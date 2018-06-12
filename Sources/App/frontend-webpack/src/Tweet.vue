<template lang="html">
  <div>
    <blockquote class=twitter-tweet>
      <div class="padding-bottom">{{tweetData}}</div>
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
  width: 468px;
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
