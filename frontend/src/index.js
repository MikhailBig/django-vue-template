// Vue 
import Vue from 'vue'

// vue-router
import VueRouter from 'vue-router'
import routes from './vue/Routes'
Vue.use(VueRouter)

const router = new VueRouter({
  routes
})

// Axios
import axios from 'axios'
Vue.prototype.$axios = axios

// Components
import App from './vue/App.vue'





new Vue({
  el: '#app',
  router,
  render: h => h(App)
})