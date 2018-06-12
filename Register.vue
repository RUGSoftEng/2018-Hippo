<template>
    <div>
        <nav-bar></nav-bar>

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
                            <label class="form-check form-check-inline">Birthday</label>
                                <!-- <span class="form-check-label"> Birthday </span> -->
                                <select name="DOBMonth">
                                	<option> - Month - </option>
                                	<option value="January">January</option>
                                	<option value="Febuary">Febuary</option>
                                	<option value="March">March</option>
                                	<option value="April">April</option>
                                	<option value="May">May</option>
                                	<option value="June">June</option>
                                	<option value="July">July</option>
                                	<option value="August">August</option>
                                	<option value="September">September</option>
                                	<option value="October">October</option>
                                	<option value="November">November</option>
                                	<option value="December">December</option>
                                </select>

                                <select name="DOBDay">
                                	<option> - Day - </option>
                                	<option value="1">1</option>
                                	<option value="2">2</option>
                                	<option value="3">3</option>
                                	<option value="4">4</option>
                                	<option value="5">5</option>
                                	<option value="6">6</option>
                                	<option value="7">7</option>
                                	<option value="8">8</option>
                                	<option value="9">9</option>
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

                                <select name="DOBYear">
                                	<option> - Year - </option>
                                  <option value="1992">2018</option>
                                  <option value="1991">2017</option>
                                  <option value="1990">2016</option>
                                  <option value="1989">2015</option>
                                  <option value="1993">2014</option>
                                  <option value="1992">2013</option>
                                  <option value="1991">2012</option>
                                  <option value="1990">2011</option>
                                  <option value="1989">2010</option>
                                  <option value="1993">2009</option>
                                  <option value="1992">2008</option>
                                  <option value="1991">2007</option>
                                  <option value="1990">2006</option>
                                  <option value="1989">2005</option>
                                  <option value="1993">2004</option>
                                  <option value="1992">2003</option>
                                  <option value="1991">2002</option>
                                  <option value="1990">2001</option>
                                  <option value="1989">2000</option>
                                  <option value="1988">1999</option>
                                  <option value="1987">1998</option>
                                  <option value="1986">1997</option>
                                  <option value="1985">1996</option>
                                  <option value="1984">1995</option>
                                  <option value="1983">1994</option>
                                	<option value="1993">1993</option>
                                	<option value="1992">1992</option>
                                	<option value="1991">1991</option>
                                	<option value="1990">1990</option>
                                	<option value="1989">1989</option>
                                	<option value="1988">1988</option>
                                	<option value="1987">1987</option>
                                	<option value="1986">1986</option>
                                	<option value="1985">1985</option>
                                	<option value="1984">1984</option>
                                	<option value="1983">1983</option>
                                	<option value="1982">1982</option>
                                	<option value="1981">1981</option>
                                	<option value="1980">1980</option>
                                	<option value="1979">1979</option>
                                	<option value="1978">1978</option>
                                	<option value="1977">1977</option>
                                	<option value="1976">1976</option>
                                	<option value="1975">1975</option>
                                	<option value="1974">1974</option>
                                	<option value="1973">1973</option>
                                	<option value="1972">1972</option>
                                	<option value="1971">1971</option>
                                	<option value="1970">1970</option>
                                	<option value="1969">1969</option>
                                	<option value="1968">1968</option>
                                	<option value="1967">1967</option>
                                	<option value="1966">1966</option>
                                	<option value="1965">1965</option>
                                	<option value="1964">1964</option>
                                	<option value="1963">1963</option>
                                	<option value="1962">1962</option>
                                	<option value="1961">1961</option>
                                	<option value="1960">1960</option>
                                	<option value="1959">1959</option>
                                	<option value="1958">1958</option>
                                	<option value="1957">1957</option>
                                	<option value="1956">1956</option>
                                	<option value="1955">1955</option>
                                	<option value="1954">1954</option>
                                	<option value="1953">1953</option>
                                	<option value="1952">1952</option>
                                	<option value="1951">1951</option>
                                	<option value="1950">1950</option>
                                	<option value="1949">1949</option>
                                	<option value="1948">1948</option>
                                	<option value="1947">1947</option>

                                </select>
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
                email: '',
                password: ''
            }
        },
        methods: {
            register: function () {
                const {first_name, last_name, email, password} = this;

                const self = this;

                axios.post('http://localhost:5000/api/users',  {
                    first_name: first_name,
                    last_name: last_name,
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
