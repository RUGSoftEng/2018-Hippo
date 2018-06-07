<template lang="html">
  <div>
    <blockquote class=tweet>
      <div style="padding-bottom: 1rem;">{{tweetData}}</div>
    </blockquote>
  </div>
</template>

<script>
export default {
  props: ['tweetData'],

}
</script>

<style scoped lang="css">
blockquote.tweet {
     display: inline-block;
     color: black;
     font-size: 20px;
     line-height: 24px;
     border-radius: 10px;
     border: 5px solid rgba(255, 0, 0, 0.75);
     box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
     margin: 10px 5px;
     padding: 16px 16px 16px 16px;
     width: 468px;
     background-color: white;
 }

blockquote.tweet p {
  font-size: 16px;
  font-weight: normal;
  line-height: 20px;
}

blockquote.tweet a {
  color: inherit;
  font-weight: normal;
  text-decoration: none;
  outline: 0 none;
}

blockquote.tweet a:hover,
blockquote.tweet a:focus {
  text-decoration: underline;
}
</style>
