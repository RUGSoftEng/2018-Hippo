<template lang="html">

  <!-- 11 - contained in center example -->
  <nav class="navbar navbar-expand-sm hippo-navbar" data-toggle="affix">
    <div class="mx-auto d-sm-flex d-block flex-sm-nowrap">
      <a class="navbar-brand" style="padding-bottom: 0; margin-right: 50px;" @click="backToHome()"><img style="height: 40px" src="../src/assets/Logo.svg"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample11" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse text-center" id="navbarsExample11">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" @click="backToHome()">Search</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="http://www.juicystory.nl/blog/">Blog</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="mailto:hippo@juicystory.nl">Support</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" @click="logout()">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>


</template>

<script>
export default {
  methods: {
    logout(){
      this.$router.push("/");
    },
    backToHome() {
      this.$router.push('/app');
    }

  }
}
</script>

<style scoped lang="css">
  .hippo-navbar
  {
    background-color: rgba(0, 0, 0, 0.75) !important;
    padding: 2px 0 0;
  }

  .hippo-nav-link
  {
    font-size: 16px;
    color: white !important;
    margin-left: 30px;
    margin-right: 30px;
    cursor: pointer;
  }

  .hippo-nav-logo
  {
    height: 40px;
    cursor: pointer;
  }
</style>
