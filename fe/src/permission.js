import router from './router'
import store from './store'
import { getToken } from '@/utils/auth' // 验权

router.beforeEach((to, from, next) => {
	if(getToken()) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      // if (store.getters.is_staff) {
      //   store.dispatch('GetUserInfo').then()
      //   next()
      // }
      next()
    }
  } else {
    if (to.meta.requireAuth) { // 在免登录白名单，直接进入
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    } else {
      next()
    }
  }
})
