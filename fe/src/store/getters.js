const getters = {
  user: state => state.user,
  auth_token: state => state.user.auth_token,
  student_id: state => state.user.student_id,
  username: state => state.user.username,
  email: state => state.user.email,
  mobile: state => state.user.mobile,
  is_staff: state => state.user.is_staff
}
export default getters
