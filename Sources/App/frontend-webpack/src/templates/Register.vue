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
                            <label class="form-check form-check-inline">Birthday</label>
                            <!-- <span class="form-check-label"> Birthday </span> -->
                            <select name="birthday-day" title="Day" v-model="birthday_day" required>
                                <option value="01">1</option>
                                <option value="02">2</option>
                                <option value="03">3</option>
                                <option value="04">4</option>
                                <option value="05">5</option>
                                <option value="06">6</option>
                                <option value="07">7</option>
                                <option value="08">8</option>
                                <option value="09">9</option>
                                <option value="10">10</option>
                                <option value="11">11</option>
                                <option value="12">12</option>
                                <option value="13">13</option>
                                <option value="14">14</option>
                                <option value="15">15</option>
                                <option value="16">16</option>
                                <option value="17">17</option>
                                <option value="18">18</option>
                                <option value="19">19</option>
                                <option value="20">20</option>
                                <option value="21">21</option>
                                <option value="22">22</option>
                                <option value="23">23</option>
                                <option value="24">24</option>
                                <option value="25">25</option>
                                <option value="26">26</option>
                                <option value="27">27</option>
                                <option value="28">28</option>
                                <option value="29">29</option>
                                <option value="30">30</option>
                                <option value="31">31</option>
                            </select>
                            <select name="birthday-month" title="Month" v-model="birthday_month" required>
                                <option value="01">January</option>
                                <option value="02">February</option>
                                <option value="03">March</option>
                                <option value="04">April</option>
                                <option value="05">May</option>
                                <option value="06">June</option>
                                <option value="07">July</option>
                                <option value="08">August</option>
                                <option value="09">September</option>
                                <option value="10">October</option>
                                <option value="11">November</option>
                                <option value="12">December</option>
                            </select>
                            <select name="birthday-year" title="Year" v-model="birthday_year" required>
                                <option v-for="year in years" :value="year">{{ year }}</option>
                            </select>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <label>Create password</label>
                            <input v-model="password" class="form-control" type="password" required>
                        </div> <!-- form-group end.// -->
                        <div class="form-group">
                            <div class="checkbox mb-3">
                                <label>
                                    <input type="checkbox" style="color: black !important;" v-model="marketing_consent"> I want to receive marketing emails from Hippo.
                                </label>
                            </div>
                            <div class="checkbox mb-3">
                                <label>
                                    <input type="checkbox" style="color: black !important;" v-model="data_collection_consent"> I give consent to use my data to generate demographics.
                                </label>
                            </div>
                        </div>
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
        computed : {
            years() {
                const year = new Date().getFullYear();
                return Array.from({length: year - (year - 100)}, (value, index) => (year - 13) - index)
            }
        },
        data() {
            return {
                isLoggedIn: store.state.isLoggedIn,

                first_name: '',
                last_name: '',
                gender: '',
                birthday_day: '',
                birthday_month: '',
                birthday_year: '',
                email: '',
                password: '',
                marketing_consent: true,
                data_collection_consent: true,
            }
        },
        methods: {
            register: function () {
                const {first_name, last_name, gender, email, password, birthday_day, birthday_month, birthday_year, data_collection_consent, marketing_consent} = this;

                const self = this;

                document.getElementById("error-window").style.display = "none";

                axios.post('http://localhost:5000/api/users', {
                    first_name: first_name,
                    last_name: last_name,
                    gender: gender,
                    email: email,
                    birthday: birthday_year + "-" + birthday_month +  "-" + birthday_day,
                    password: password,
                    data_collection_consent: data_collection_consent,
                    marketing_consent: marketing_consent
                })
                    .then(function (response) {
                        console.log(response);

                        self.redirect();
                    })
                    .catch(function (error) {
                        console.log(error);

                        document.getElementById("error-window").style.display = "block";

                        if (typeof error.response.data.message !== "undefined") {
                            document.getElementById("error-window").innerHTML = error.response.data.message;
                        }
                        else {
                            document.getElementById("error-window").innerHTML = "An unknown exception occurred, there could be a issue with connecting to the server.";
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
