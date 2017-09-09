import fetch from '@/utils/fetch'

export function getProblemList(page, page_size) {
  return fetch({
    url: '/problems/',
    method: 'get',
    params: { page, page_size }
  })
}

export function getProblemDetail(number) {
  return fetch({
    url: '/problems/' + number + '/',
    method: 'get'
  })
}