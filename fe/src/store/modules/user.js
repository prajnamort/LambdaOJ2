import { loginByUsername, logout, getUserInfo, changePassword } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'

const user = {
  state: {
    auth_token: getToken(),
    student_id: '',
    username: '',
    email: '',
    mobile: '',
    is_staff: null
  },

  mutations: {
  	SET_AUTH_TOKEN: (state, auth_token) => {
      state.auth_token = auth_token
    },
    SET_USERNAME: (state, username) => {
      state.username = username
    },
    SET_STUDENT_ID: (state, student_id) => {
      state.student_id = student_id
    },
    SET_EMAIL: (state, email) => {
      state.email = email
    },
    SET_MOBILE: (state, mobile) => {
      state.mobile = mobile
    },
    SET_IS_STAFF: (state, is_staff) => {
      state.is_staff = is_staff
    }
  },

  actions: {
    LoginByUsername({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        loginByUsername(username, userInfo.password).then(response => {
          const data = response.data
          setToken(data.auth_token)
          console.log(data)
          commit('SET_AUTH_TOKEN', data.auth_token)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    GetUserInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getUserInfo(state.auth_token).then(response => {
          const data = response.data
          commit('SET_USERNAME', data.username)
          commit('SET_STUDENT_ID', data.student_id)
          commit('SET_EMAIL', data.email)
          commit('SET_MOBILE', data.mobile)
          commit('SET_IS_STAFF', data.is_staff)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },
    LogOut({ commit, state }) {
      return new Promise((resolve, reject) => {
        logout(state.auth_token).then(() => {
          commit('SET_AUTH_TOKEN', '')
          commit('SET_USERNAME', '')
          commit('SET_STUDENT_ID', '')
          commit('SET_EMAIL', '')
          commit('SET_MOBILE', '')
          commit('SET_IS_STAFF', false)
          removeToken()
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    FeLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_AUTH_TOKEN', '')
        removeToken()
        resolve()
      })
    },
    ChangePassword({commit}, passwordInfo) {
      console.log(passwordInfo)
      return new Promise((resolve, reject) => {
        changePassword(passwordInfo.current_password,
                       passwordInfo.new_password,
                       passwordInfo.re_new_password).then(response => {
          const data = response.data
          console.log(data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}

export default user