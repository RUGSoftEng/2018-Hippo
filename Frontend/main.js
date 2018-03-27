Vue.component('nav-bar', {
  template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#">Hippo<!--<img src="Assets/Hippo-Poster.png" alt="" width="100"> --></a>
        <div class="container">
          <form class="form-inline">
            <input class="form-control mr-sm-3" type="search" placeholder="Search for tweets..." aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>




  <!--
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
    -->
  `
})

Vue.component('logo-poster', {
  template: `
    <header class="business-header">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <h1 class="display-3 text-center text-white mt-4"></h1>
          </div>
        </div>
      </div>
    </header>
  `
})

Vue.component('search-bar', {
  template: `
    <div class="container center">
      <form class="form-inline">
        <input class="form-control mr-sm-3" type="search" placeholder="Search for tweets..." aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  `
})

Vue.component('tweet-list', {
  props: ['tweetList'],
  template:`
    <section class="py-5">
      <div class="container text-center">
        <tweet v-for="t in tweetList" :tweetData=t></tweet>
      </div>
    </section>
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
      <!-- <nav-bar></nav-bar> -->
      <logo-poster></logo-poster>
      <center>
        <h1 id="tweetTitle">Tweets</h1>
        <search-bar></search-bar>
      </center>
      <tweet-list :tweetList="$data.tweetList"></tweet-list>
    </div>
  `
})
new Vue({
  el: "#root"
})
