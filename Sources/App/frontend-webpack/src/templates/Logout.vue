<template>
    <div>
        <p>You should be redirected within a few seconds...</p>
    </div>
</template>

<script>
    import store from '../store'

    export default {
        store,
        methods: {
            logout: function () {
                this.$store.dispatch('logout').then(() => {
                    self.redirect();
                    location.reload();
                });
            },
            redirect: function () {
                this.$router.push("/");
            }
        },
        beforeMount(){
            this.logout()
        },
    }
</script>

<style scoped>

</style>