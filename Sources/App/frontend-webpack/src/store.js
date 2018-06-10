import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isLoggedIn: !!localStorage.getItem("token")
    },
    actions: {
        login(token) {
            localStorage.setItem("token", token);
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