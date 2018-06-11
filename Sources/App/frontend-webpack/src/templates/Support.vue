<template>
    <div>
        <nav-bar></nav-bar>
        <div class="row  d-flex justify-content-center" style="color: black !important; margin-top: 100px;">
            <h1 class="display-4">Support</h1>
        </div>
        <div class="container d-flex justify-content-center" style="margin-top: 100px;">
            <div class="row" style="color: black !important;">
                <div class="col-4">
                    <div class="card text-center" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">Special title treatment</h5>
                            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="card text-center" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">Special title treatment</h5>
                            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="card text-center" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">Contact us</h5>
                            <p class="card-text">You can contact us by email.</p>
                            <a href="#" class="btn btn-primary">Email</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue';

    export default {
        components: {
            'nav-bar': NavBar,
        }
    }
</script>

<style scoped>

</style>