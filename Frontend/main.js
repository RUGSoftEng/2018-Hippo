Vue.component('nav-bar', {
  template: `
    <div class="container">
      <nav class="navbar navbar-light">
        <a class="navbar-brand" href="#">
          <img src="/assets/Hippo_logo_2.png" width="50" height="60" alt="">
          Hippo
          </img>
        </a>
        <form class="form-inline">
          <input class="form-control mr-sm-3" type="search" placeholder="Search for tweets..." aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </nav>
    </div>
  `
})

Vue.component('tweet-list', {
  props: ['tweetList'],
  template:`
    <div class="container text-center">
      <tweet v-for="t in tweetList" :tweetData=t></tweet>
    </div>
  `
})

Vue.component('tweet', {
  props: ['tweetData'],
  template:`
    <div>
      <blockquote class=twitter-tweet>
        <div class="padding-bottom">{{tweetData}}</div>
        <a href="">-By some random guy with 0 followers</a>
      </blockquote>
    </div>
  `
})


Vue.component('layout', {
  data() {
    return {
      tweetList: ["Some random business idea nobody cares about", "Some random business idea nobody cares about", "Some random business idea nobody cares about"]
    };
  },

  template:`
    <div>
      <nav-bar></nav-bar>
      <tweet-list :tweetList="$data.tweetList"></tweet-list>
    </div>
  `
})
new Vue({
  el: "#root"
})
