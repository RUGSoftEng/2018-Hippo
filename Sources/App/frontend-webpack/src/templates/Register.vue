<template>
    <div>
        <nav-bar></nav-bar>
        <div id="error-window" class="alert alert-danger" role="alert" style="margin: 10px; display: none;">
        </div>
        <div class="d-flex justify-content-center" style="margin-top: 100px;">
            <div class="card" style="width: 500px; color: black !important;">
                <header class="card-header text-center">
                    <h2 class="h3 mb-3 font-weight-normal" style="margin-top: 20px;">Sign up</h2>
                </header>
                <article class="card-body">
                    <form @submit.prevent="register()">
                        <div class="form-row">
                            <div class="col form-group">
                                <label>First name</label>
                                <input v-model="first_name" type="text" class="form-control" placeholder="" required
                                       autofocus name="name">
                            </div> <!-- form-group end.// -->
                            <div class="col form-group">
                                <label>Last name</label>
                                <input v-model="last_name" type="text" class="form-control" placeholder="" required
                                       name="family-name">
                            </div> <!-- form-group end.// -->
                        </div> <!-- form-row end.// -->
                        <div class="form-group">
                            <label>Email address</label>
                            <input v-model="email" type="email" class="form-control" placeholder="" required
                                   name="email">
                            <small class="form-text text-muted">We'll never share your email with anyone
                                else.
                            </small>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <label class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="gender" value="m" v-model="gender"
                                       required>
                                <span class="form-check-label"> Male </span>
                            </label>
                            <label class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="gender" value="f" v-model="gender"
                                       required>
                                <span class="form-check-label"> Female</span>
                            </label>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <label>Create password</label>
                            <input v-model="password" class="form-control" type="password" required>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <button type="submit" class="btn btn-primary btn-block">Register</button>
                        </div> <!-- form-group// -->
                        <small class="text-muted">By clicking the 'Sign Up' button, you confirm that you accept our <br>
                            Terms of use and Privacy Policy.
                        </small>
                    </form>
                </article> <!-- card-body end .// -->
                <div class="border-top card-body text-center">Have an account?
                    <router-link to="/login">Log In</router-link>
                </div>
            </div> <!-- card.// -->
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

                first_name: '',
                last_name: '',
                gender: '',
                email: '',
                password: ''
            }
        },
        methods: {
            register: function () {
                const {first_name, last_name, gender, email, password} = this;

                const self = this;

                document.getElementById("error-window").style.display = "none";

                axios.post('http://localhost:5000/api/users', {
                    first_name: first_name,
                    last_name: last_name,
                    gender: gender,
                    email: email,
                    password: password,
                    data_collection_consent: true,
                    marketing_consent: true
                })
                    .then(function (response) {
                        console.log(response);

                        self.redirect();
                    })
                    .catch(function (error) {
                        console.log(error);

                        document.getElementById("error-window").style.display = "block";

                        if (typeof error.response !== "undefined") {
                            document.getElementById("error-window").innerHTML = error.response.data.message;
                        }
                        else {
                            document.getElementById("error-window").innerHTML = "An unknown exception occurred.";
                        }
                    });

            },
            redirect: function () {
                this.$router.push("/login");
            }
        },
        beforeMount() {
            if (this.isLoggedIn) {
                this.redirect();
            }
        },
    }
</script>

<style scoped>

</style>