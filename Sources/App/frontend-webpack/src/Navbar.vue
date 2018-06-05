<template lang="html">

  <!-- 11 - contained in center example -->
  <nav class="navbar navbar-expand-sm hippo-navbar" data-toggle="affix">
    <div class="mx-auto d-sm-flex d-block flex-sm-nowrap">
      <a class="navbar-brand" style="padding-bottom: 0; margin-right: 50px;" href="#"><img style="height: 40px" src="../src/assets/Logo.svg"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample11" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse text-center" id="navbarsExample11">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link hippo-nav-link" href="#">Explore</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="#">Search</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="#">Blog</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="#">Support</a>
          </li>
          <li class="nav-item">

            <a class="nav-link hippo-nav-link" href="#"><img style="height: 28px; padding-right: 20px;" src="../src/assets/icons8-male-user-filled.svg">Account</a>
          </li>
          <li class="nav-item">
            <a class="nav-link hippo-nav-link" href="#">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>


</template>

<script>
export default {
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
  }
</style>
