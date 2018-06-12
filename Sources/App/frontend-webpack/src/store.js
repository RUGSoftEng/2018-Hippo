import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isLoggedIn: !!localStorage.getItem("token")
    },
    actions: {
        login(toke) {
            console.log(toke);
            localStorage.setItem("token", toke);
        },
        logout() {
            localStorage.removeItem("token");
        }
    },
    getters: {
        token: string => {
            return localStorage.getItem("token");
        }
    }
});