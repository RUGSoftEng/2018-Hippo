<template lang="html">
    <div>
        <nav-bar></nav-bar>

        <header class="masthead">
            <div class="container h-100">
                <div class="row h-100">
                    <div class="col-lg-7 my-auto">
                        <div class="header-content mx-auto">
                            <h1 class="mb-5 home-header" style="color: white !important;">Welcome to Hippo</h1>
                            <h3 class="home-header" style="margin-bottom: 75px; color: white !important;">Develop and
                                validate startup ideas.</h3>
                            <router-link to="/register" class="btn btn-outline btn-xl js-scroll-trigger signup-link">Sign up
                                now</router-link>
                        </div>
                    </div>
                    <div class="col-lg-5 my-auto">
                        <div class="device">
                            <!-- Demo image for screen mockup, you can put an image here, some HTML, an animation, video, or anything else! -->
                            <!-- <img src="img/Hippo_Logo_2.png" class="img-fluid" alt=""> -->
                            <img src="src/assets/Hippo_Logo_1.png" class="img-fluid" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <section class="features" id="features">
            <div class="container">
                <div class="section-heading text-center">
                    <h2 style="color: black !important;">Check out what you can do with Hippo!</h2>
                    <hr>
                </div>
                <div class="row">
                    <div class="col-lg-8 my-auto" style="width:800px; margin:0 auto;">
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-lg-6">
                                    <div class="feature-item">
                                        <i class="icon-present text-primary"></i>
                                        <h3 style="color: black !important;">Explore ideas</h3>
                                        <p class="text-muted quote-feature" style="line-height: 1.6; margin-top: 25px;">
                                            Hippo allows you to explore ideas that are based on data from Twitter.</p>
                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="feature-item">
                                        <i class="icon-screen-smartphone text-primary"></i>
                                        <h3 style="color: black !important;">Search in our data</h3>
                                        <p class="text-muted quote-feature" style="line-height: 1.6; margin-top: 25px;">
                                            You can not only search for ideas, but also access the actual tweets behind
                                            them.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-6">
                                    <div class="feature-item">
                                        <i class="icon-social-twitter text-primary"></i>
                                        <h3 style="color: black !important;">Data from Twitter</h3>
                                        <p class="text-muted quote-feature" style="line-height: 1.6; margin-top: 25px;">
                                            Giving you access to the minds of more than 300 million active users.</p>
                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="feature-item">
                                        <i class="icon-like text-primary"></i>
                                        <h3 style="color: black !important;">Interact with ideas</h3>
                                        <p class="text-muted quote-feature" style="line-height: 1.6; margin-top: 25px;">
                                            You can like and save ideas, or talk to other users about them.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <footer>
            <div class="container">
                <p>&copy; Hippo 2018. All Rights Reserved.</p>
                <ul class="list-inline">
                    <li class="list-inline-item">
                        <a href="#">Privacy</a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#">Terms</a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#">FAQ</a>
                    </li>
                </ul>
            </div>
        </footer>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue';

    export default {
        components: {
            'nav-bar': NavBar,
        },

        data() {
            return {
                username: "",
                password: "",
                confirmedPassword: ""
            }
        },

        methods: {}
    }
</script>

<style lang="css">

    .signup-form {
        margin: 5% auto;
        width: 600px;
        height: 450px;
        padding: 40px;
        background-color: #F5F5F5;
        border-radius: 10px;
    }

    .signup-form-field {
        margin-bottom: 20px;
        padding: 4px 10px;
        height: 32px;
        width: 100%;
        border: #D1D1D1 solid 0.1em;
        border-radius: 4px;
        font-weight: 400;
        font-size: 15px;
        transition: 0.2s ease;
    }

    hr {
        max-width: 100px;
        margin: 25px auto 0;
        border: 1px rgba(34, 34, 34, 0.1);
    }

    .home-header {
        font-family: 'Catamaran', 'Helvetica', 'Arial', 'sans-serif';
        font-weight: 200;
        letter-spacing: 1px;
        color: black !important;
    }

    .quote-feature {
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    section {
        padding: 100px 0;
    }

    section h2 {
        font-size: 50px;
    }

    header.masthead {
        position: relative;
        width: 100%;
        padding-top: 150px;
        padding-bottom: 100px;
        color: white;
        background: url("../assets/bg-pattern.png"), linear-gradient(to left, #7b4397, #dc2430);
    }

    header.masthead .header-content {
        max-width: 500px;
        margin-bottom: 100px;
        text-align: center;
    }

    header.masthead .header-content h1 {
        font-size: 30px;
    }

    header.masthead .device-container {
        max-width: 325px;
        margin-right: auto;
        margin-left: auto;
    }

    header.masthead .device-container img {
        border-radius: 3px;
    }

    @media (min-width: 992px) {
        header.masthead {
            height: 100vh;
            min-height: 775px;
            padding-top: 0;
            padding-bottom: 0;
        }

        header.masthead .header-content {
            margin-bottom: 0;
            text-align: left;
        }

        header.masthead .header-content h1 {
            font-size: 50px;
        }

        header.masthead .device-container {
            max-width: 325px;
        }
    }

    section.download {
        position: relative;
        padding: 150px 0;
    }

    section.download h2 {
        font-size: 50px;
        margin-top: 0;
    }

    section.download .badges .badge-link {
        display: block;
        margin-bottom: 25px;
    }

    section.download .badges .badge-link:last-child {
        margin-bottom: 0;
    }

    section.download .badges .badge-link img {
        height: 60px;
    }

    @media (min-width: 768px) {
        section.download .badges .badge-link {
            display: inline-block;
            margin-bottom: 0;
        }
    }

    @media (min-width: 768px) {
        section.download h2 {
            font-size: 70px;
        }
    }

    section.features .section-heading {
        margin-bottom: 100px;
    }

    section.features .section-heading h2 {
        margin-top: 0;
    }

    section.features .section-heading p {
        margin-bottom: 0;
    }

    section.features .device-container,
    section.features .feature-item {
        max-width: 325px;
        margin: 0 auto;
    }

    section.features .device-container {
        margin-bottom: 100px;
    }

    @media (min-width: 992px) {
        section.features .device-container {
            margin-bottom: 0;
        }
    }

    section.features .feature-item {
        padding-top: 50px;
        padding-bottom: 50px;
        text-align: center;
    }

    section.features .feature-item h3 {
        font-size: 30px;
    }

    section.features .feature-item i {
        font-size: 80px;
        display: block;
        margin-bottom: 15px;
        background: -webkit-linear-gradient(to left, #7b4397, #dc2430);
        background: linear-gradient(to left, #7b4397, #dc2430);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    section.cta {
        position: relative;
        padding: 250px 0;
        background: url("../assets/bg-cta.jpg") center;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }

    section.cta .cta-content {
        position: relative;
        z-index: 1;
    }

    section.cta .cta-content h2 {
        font-size: 50px;
        max-width: 450px;
        margin-top: 0;
        margin-bottom: 25px;
        color: white;
    }

    @media (min-width: 768px) {
        section.cta .cta-content h2 {
            font-size: 80px;
        }
    }

    section.contact h2 {
        margin-top: 0;
        margin-bottom: 25px;
    }

    section.contact h2 i {
        color: #dd4b39;
    }

    section.contact ul.list-social li a {
        font-size: 40px;
        line-height: 80px;
        display: block;
        width: 80px;
        height: 80px;
        color: white;
        border-radius: 100%;
    }

    section.contact ul.list-social li.social-twitter a {
        background-color: #1da1f2;
    }

    section.contact ul.list-social li.social-twitter a:hover {
        background-color: #0d95e8;
    }

    section.contact ul.list-social li.social-facebook a {
        background-color: #3b5998;
    }

    section.contact ul.list-social li.social-facebook a:hover {
        background-color: #344e86;
    }

    section.contact ul.list-social li.social-google-plus a {
        background-color: #dd4b39;
    }

    section.contact ul.list-social li.social-google-plus a:hover {
        background-color: #d73925;
    }

    footer {
        padding: 25px 0;
        text-align: center;
        color: rgba(255, 255, 255, 0.3);
        background-color: #222222;
    }

    footer p {
        font-size: 12px;
        margin: 0;
    }

    footer ul {
        margin-bottom: 0;
    }

    footer ul li a {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.3);
    }

    footer ul li a:hover, footer ul li a:focus, footer ul li a:active, footer ul li a.active {
        text-decoration: none;
    }

    .bg-primary {
        background: #fdcc52;
        background: -webkit-linear-gradient(#fdcc52, #fdc539);
        background: linear-gradient(#fdcc52, #fdc539);
    }

    .text-primary {
        color: #fdcc52;
    }

    .no-gutter > [class*='col-'] {
        padding-right: 0;
        padding-left: 0;
    }

    .signup-link {
        color: white;
        border: 1px solid white;
        background-color: rgba(255, 255, 255, 0.25);
    }

    .signup-link:hover, .signup-link:focus, .signup-link:active {
        color: white;
        border-color: #fdcc52;
        background-color: #fdcc52;
    }

    .signup-link {
        border-radius: 300px;
        font-family: 'Lato', 'Helvetica', 'Arial', 'sans-serif';
        letter-spacing: 2px;
    }

    .signup-link {
        font-weight: bold;
        font-size: 16px;
        padding: 15px 45px;
    }

</style>
