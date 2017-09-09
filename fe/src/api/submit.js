import fetch from '@/utils/fetch'

export function submitProblem(problem, language, code) {
  const data = {
    problem,
    language,
    code
  }
  return fetch({
    url: '/submits/',
    method: 'post',
    data
  })
}

export function getSubmitDetail(id) {
  return fetch({
    url: '/submits/' + id + '/',
    method: 'get'
  })
}

export function getSubmitList(page, page_size) {
  return fetch({
    url: '/my/submits/',
    method: 'get',
    params: { page, page_size }
  })
}
