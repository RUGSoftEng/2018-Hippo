<template>
    <div id="app">
        <nav-bar></nav-bar>
        <div>
            <search-bar></search-bar>
        </div>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue';
    import SearchBar from '../components/SearchBar.vue';

    export default {
        components: {
            'nav-bar': NavBar,
            'search-bar': SearchBar
        }
    }
</script>

<style>

</style>
