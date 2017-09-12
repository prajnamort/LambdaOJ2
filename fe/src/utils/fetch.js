import axios from 'axios'
import router from '@/router'
import store from '@/store'
import { getToken } from '@/utils/auth'

// 创建axios实例
const service = axios.create({
  baseURL: __API__, // api的base_url
  timeout: 5000                  // 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  // 让每个请求都携带token
  if (store.getters.auth_token) {
    config.headers['Authorization'] = 'TOKEN ' + getToken()
  }
  return config
}, error => {
  console.log(error) // for debug
  Promise.reject(error)
})

// respone拦截器
service.interceptors.response.use(
  response => response,
  error => {
    console.log(error.response)// for debug
    if (error.response.status === 429 || error.response.status >= 500) {
    	alert(error.response.data.detail)
    } else if (error.response.status === 404) {
      router.push({ path: '/404' })
    }
    return Promise.reject(error)
  }
)

export default service
