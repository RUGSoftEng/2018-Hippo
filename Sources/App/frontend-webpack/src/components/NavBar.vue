<template lang="html">
    <nav class="navbar navbar-expand-sm hippo-navbar" data-toggle="affix">
        <div class="mx-auto d-sm-flex d-block flex-sm-nowrap">
            <router-link class="navbar-brand" style="padding-bottom: 0; margin-left: 100px;" to="/"><img
                    style="height: 40px" src="../assets/Logo.svg"></router-link>
            <div class="collapse navbar-collapse text-center">
                <ul class="navbar-nav">
                    <li style="width: 25px;"></li>
                    <li class="nav-item">
                        <router-link class="nav-link hippo-nav-link" to="/app/explore">Explore</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link hippo-nav-link" to="/app/search">Search</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link hippo-nav-link" href="http://www.juicystory.nl/blog/">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link hippo-nav-link" href="mailto:hippo@juicystory.nl">Support</a>
                    </li>
                    <li style="width: 25px;"></li>
                    <li class="nav-item" v-if="isLoggedIn">
                        <router-link class="nav-link hippo-nav-link" to="/account"><img
                                style="height: 24px; margin-right: 10px;" src="../assets/icons8-male-user-filled.svg">Account
                        </router-link>
                    </li>
                    <li class="nav-item" v-if="isLoggedIn">
                        <router-link class="nav-link hippo-nav-link" to="/logout">Logout</router-link>
                    </li>
                    <li class="nav-item" v-if="!isLoggedIn">
                        <router-link class="nav-link hippo-nav-link" to="/login">Login</router-link>
                    </li>
                    <li class="nav-item" v-if="!isLoggedIn">
                        <router-link class="nav-link hippo-nav-link" to="/register">Register</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>


</template>

<script>
    import store from '../store'

    export default {
        store,
        data() {
            return {
                isLoggedIn: store.state.isLoggedIn
            }
        }
    }
</script>

<style scoped lang="css">
    .hippo-navbar {
        background-color: rgba(0, 0, 0, 0.75) !important;
        padding: 2px 0 0;
    }

    .hippo-nav-link {
        font-size: 16px;
        color: white !important;
        margin-left: 30px;
        margin-right: 30px;
        cursor: pointer;
    }

    .hippo-nav-logo {
        height: 40px;
        cursor: pointer;
    }
</style>
