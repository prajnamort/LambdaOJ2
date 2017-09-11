import router from './router'
import store from './store'
import { getToken } from '@/utils/auth' // 验权

router.beforeEach((to, from, next) => {
	if(getToken()) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      next()
    }
  } else {
    if (to.meta.requireAuth) { // 进入这些网页需要登录
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    } else {
      next()
    }
  }
})
