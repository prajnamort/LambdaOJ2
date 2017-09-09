// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VeeValidate from 'vee-validate'
import VueHighlightJS from 'vue-highlightjs'
import App from './App'
import router from './router'
import store from './store'
import * as filters from './filters' // 全局filter
import './permission'

// register global utility filters.
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

Vue.use(VeeValidate)
Vue.use(VueHighlightJS,['cpp'])

Vue.config.productionTip = false

/* eslint-disable no-new */
const app = new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
