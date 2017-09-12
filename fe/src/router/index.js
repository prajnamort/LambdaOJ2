import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const Index = () => import('../views/Index.vue')
const Login = () => import('../views/Login.vue')
const ProblemDetail = () => import('../views/ProblemDetail.vue')
const ChangePassword = () => import('../views/ChangePassword.vue')
const PersonalInfo = () => import('../views/PersonalInfo.vue')
const SubmitDetail = () => import('../views/SubmitDetail.vue')
const SubmitList = () => import('../views/SubmitList.vue')
const Profile = () => import('../views/Profile.vue')
const ErrorPage404 = () => import('../views/404.vue')

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
    	path: '/login',
      name: 'Login',
    	component: Login
    },
    {
      path: '/404',
      name: 'ErrorPage404',
      component: ErrorPage404
    },
    {
      path: '/problem/:number(\\d+)',
      name: 'ProblemDetail',
      meta: {
        requireAuth: true
      },
      component: ProblemDetail
    },
    {
      path: '/submit/:id(\\d+)',
      name: 'SubmitDetail',
      meta: {
        requireAuth: true
      },
      component: SubmitDetail
    },
    {
      path: '/profile',
      name: 'Profile',
      meta: {
        requireAuth: true
      },
      component: Profile
    },
    {
      path: '/account',
      name: 'Account',
      meta: {
        requireAuth: true
      },
      component: ChangePassword
    }
  ]
})
