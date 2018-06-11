<template>
    <div>
        <nav-bar></nav-bar>
        <div id="error-window" class="alert alert-danger" role="alert" style="margin: 10px; display: none;">
        </div>
        <div class="d-flex justify-content-center" style="margin-top: 100px;">

            <div class="card" style="width: 500px; color: black !important;">
                <header class="card-header text-center">
                    <h2 class="h3 mb-3 font-weight-normal" style="margin-top: 20px;">My account</h2>
                </header>
                <article class="card-body">
                    <form @submit.prevent="update_account()">
                        <div class="form-row">
                            <div class="col form-group">
                                <label>First name</label>
                                <input v-model="first_name" type="text" class="form-control" placeholder="" required
                                       autofocus name="name">
                            </div> <!-- form-group end.// -->
                            <div class="col form-group">
                                <label>Last name</label>
                                <input v-model="last_name" type="text" class="form-control" placeholder="" required name="family-name">
                            </div> <!-- form-group end.// -->
                        </div> <!-- form-row end.// -->
                        <div class="form-group">
                            <label>Email address</label>
                            <input v-model="email" type="email" class="form-control" placeholder="" required name="email">
                            <small class="form-text text-muted">We'll never share your email with anyone
                                else.
                            </small>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <label class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="gender" value="option1">
                                <span class="form-check-label"> Male </span>
                            </label>
                            <label class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="gender" value="option2">
                                <span class="form-check-label"> Female</span>
                            </label>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <label>Change password</label>
                            <input v-model="password" class="form-control" type="password">
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <button type="submit" class="btn btn-primary btn-block">Save changes</button>
                        </div> <!-- form-group// -->
                    </form>
                </article> <!-- card-body end .// -->
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
                email: '',
                password: '',
            }
        },
        methods: {
            update_account: function () {
                const {first_name, last_name, email, password} = this;

                document.getElementById("error-window").style.display = "none";

                axios.post('http://localhost:5000/api/user/account',  {
                    auth:{
                        username: store.getters.token,
                    },

                    first_name: first_name,
                    last_name: last_name,
                    email: email,
                    password: password,
                    data_collection_consent: true,
                    marketing_consent: true,

                })
                    .then(function (response) {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);

                        document.getElementById("error-window").style.display = "block";
                        document.getElementById("error-window").innerHTML = error.response.data.message;
                    });

            },
            get_account: function () {
                const self = this;

                console.log("dd" + store.getters.token);
                axios.get('http://localhost:5000/api/user/account',  {
                    auth:{
                        username: store.getters.token,
                    }
                })
                    .then(function (response) {
                        console.log(response);

                        self.first_name = response.data.first_name;
                        self.last_name = response.data.last_name;
                        self.email = response.data.email;
                        self.data_collection_consent = response.data.data_collection_consent;
                        self.marketing_consent = response.data.marketing_consent;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });

            },
            redirect: function () {
                this.$router.push("/login");
            }
        },
        beforeMount() {
           this.get_account();
        },
    }
</script>


<style scoped>

</style>