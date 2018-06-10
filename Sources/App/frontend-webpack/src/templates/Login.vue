<template lang="html">
    <div>
        <nav-bar></nav-bar>

        <div class="text-center" style="color: black !important;">
            <form class="form-signin" @submit.prevent="login()">
                <img style="height: 100px; margin-bottom: 20px;" src="../assets/Logo-black.svg">
                <h1 class="h3 mb-3 font-weight-normal"
                    style="color: black !important; font-family: Catamaran,Helvetica,Arial,sans-serif; margin-bottom: 30px !important;">Sign in</h1>
                <label for="inputEmail" class="sr-only">Email address</label>
                <input type="email" id="inputEmail" v-model="email" class="form-control" placeholder="Email address"
                       required autofocus name="email">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="Password"
                       required>
                <div class="checkbox mb-3">
                    <label>
                        <input type="checkbox" style="color: black !important;" value="remember-me"> Remember me
                    </label>
                </div>
                <button type="submit" class="btn btn-lg btn-primary btn-block">
                    Sign in
                </button>
                <div class="text-center" style="margin-top: 30px;">Don't have an account yet? <router-link to="/register">Register</router-link></div>
            </form>
        </div>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue';
    import store from '../store'

    import axios from 'axios';

    export default {
        store,
        components: {
            'nav-bar': NavBar,
        },
        data() {
            return {
                isLoggedIn: store.state.isLoggedIn,

                email: '',
                password: ''
            }
        },
        methods: {
            login: function () {
                const { email, password } = this;

                const self = this;

                axios.get('http://localhost:5000/api/token', {
                    auth: {
                        username: email,
                        password: password
                    },
                })
                    .then(function (response) {
                        console.log(response);

                        self.$store.dispatch('login', {
                            token: response.data.token
                        }).then(() => {
                            self.redirect();
                            location.reload();
                        });
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },
            redirect: function () {
                this.$router.push("/app");
            }
        },
        beforeMount(){
            if (this.isLoggedIn){
                this.redirect();
            }
        },
    }

</script>

<style lang="css">

    .form-signin {
        width: 100%;
        max-width: 420px;
        padding: 30px 25px;
        margin: 200px auto auto;
        background-color: white;
        border-radius: 10px;
        border: rgba(0, 0, 0, 0.125) solid 1px;


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
