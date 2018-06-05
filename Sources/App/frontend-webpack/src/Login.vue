<template lang="html">
  <div class="text-center">
    <form class="form-signin">
        <img style="height: 100px; margin-bottom: 20px;" src="../src/assets/Logo-black.svg">
        <h1 class="h3 mb-3 font-weight-normal" style="font-family: Catamaran,Helvetica,Arial,sans-serif;">Sign in</h1>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="Password" required>
        <div class="checkbox mb-3">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit" @click="login()">Sign in</button>
      </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    login() {
        let cmp = this;
        console.log(cmp.username, cmp.password)
        axios.get("http://localhost:5000/api/quick/login?username=" + cmp.username + "&password=" + cmp.password).then(function (response){
          console.log(response.data);
          if(response.data.ok === "true"){
            cmp.$router.push("/app");
          } else {
            alert("Username and password combination does not exist!");
          }
        });

    },
  }
}
</script>

<style lang="css">

.form-signin {
  width: 100%;
  max-width: 420px;
  padding: 40px;
    margin: 200px auto auto;
    background-color: rgba(201, 201, 201, 0.18);
    border-radius: 10px;

}

.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}

.form-signin .form-control:focus {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

</style>
