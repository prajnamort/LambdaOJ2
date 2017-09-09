import fetch from '@/utils/fetch'

export function loginByUsername(username, password) {
  const data = {
    username,
    password
  }
  return fetch({
    url: '/auth/login/',
    method: 'post',
    data
  })
}

export function logout() {
  return fetch({
    url: '/auth/logout/',
    method: 'post'
  })
}

export function getUserInfo(token) {
  return fetch({
    url: '/my/info/',
    method: 'get'
  })
}

export function changePassword(current_password,
                               new_password,
                               re_new_password) {
  const data = {
    current_password,
    new_password,
    re_new_password
  }
  return fetch({
    url: '/auth/password/',
    method: 'post',
    data
  })
}