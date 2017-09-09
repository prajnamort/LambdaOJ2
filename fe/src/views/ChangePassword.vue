<template>
  <div class="login">
    <form class="password-form" :model="passwordForm" v-on:submit.prevent="handleChangePassword">
      <input name="current-password" type="password" v-model="passwordForm.current_password" placeholder="现密码" />
      <input name="new_password" type="password" v-model="passwordForm.new_password" placeholder="新密码" />
      <input name="re_new_password" type="password" @keyup.enter.native="handleChangePassword" v-model="passwordForm.re_new_password" placeholder="重复新密码" />
      <button type="submit">更改密码</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'change-password',
  data () {
    const validatePassword = (rule, value, callback) => {
      if (value.length < 8) {
        callback(new Error('密码不能小于8位'))
      } else {
        callback()
      }
    }
    return {
      passwordForm: {
        current_password: '',
        new_password: '',
        re_new_password: ''
      },
      // loginRules: {
      //   username: [{ required: true, trigger: 'blur', validator: validateUsername }],
      //   password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      // }
    }
  },
  methods: {
    handleChangePassword() {
      this.$store.dispatch('ChangePassword', this.passwordForm).then(() => {
        this.$store.dispatch('FeLogOut')
      }).then(() => {
        this.$router.push({ path: '/login' })
        location.reload()// 为了重新实例化vue-router对象 避免bug
      }).catch(() => {
        // this.loading = false
      })
    }
  }
}
</script>