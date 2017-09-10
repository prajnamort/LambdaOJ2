<template>
  <div class="content-wrapper change-password">
    <div class="form-wrapper">
      <form class="password-form" :model="passwordForm" @submit.prevent="handleChangePassword">
        <h2>修改密码</h2>
        <div class="error" v-if="errorDict.non_field_errors">{{ errorDict.non_field_errors[0] }}</div>
        <div class="row">
          <input v-validate="'required'" name="current_password" type="password" v-model="passwordForm.current_password" placeholder="旧密码" />
          <div class="warning" v-if="errors.has('current_password')">{{ errors.first('current_password') }}</div>
          <div class="warning" v-if="errorDict.current_password">{{ errorDict.current_password[0] }}</div>
        </div>
        <div class="row">
          <input v-validate="'required'" name="new_password" type="password" v-model="passwordForm.new_password" placeholder="新密码" />
          <div class="warning" v-if="errors.has('new_password')">{{ errors.first('new_password') }}</div>
          <div class="warning" v-if="errorDict.new_password">{{ errorDict.new_password[0] }}</div>
        </div>
        <div class="row">
          <input v-validate="'required'" name="re_new_password" type="password" @keyup.enter.native="handleChangePassword" v-model="passwordForm.re_new_password" placeholder="确认新密码" />
          <div class="warning" v-if="errors.has('re_new_password')">{{ errors.first('re_new_password') }}</div>
          <div class="warning" v-if="errorDict.re_new_password">{{ errorDict.re_new_password[0] }}</div>
        </div>
        <input class="submit-button" type="submit" value="更改密码"/>
      </form>
    </div>
  </div>
</template>

<script>
import { Validator } from 'vee-validate'

const dict = {
  en: {
    custom: {
      current_password: {
        required: '请输入旧密码'
      },
      new_password: {
        required: '请输入新密码'
        // confirmed: '密码必须相同'
      },
      re_new_password: {
        required: '请确认新密码'
      }
    }
  }
}
Validator.updateDictionary(dict)

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
      errorDict: {}
    }
  },
  methods: {
    handleChangePassword() {
      this.$store.dispatch('ChangePassword', this.passwordForm).then(() => {
        this.$store.dispatch('FeLogOut')
      }).then(() => {
        this.$router.push({ path: '/login' })
        location.reload()// 为了重新实例化vue-router对象 避免bug
      }).catch((error) => {
        this.errorDict = error.response.data
        console.log(this.errorDict.non_field_errors)
      })
    }
  }
}
</script>

<style lang="less">
.change-password {
  .form-wrapper {
    margin: 80px auto;
    position: relative;
    .password-form {
      width: 330px;
      margin: 0 auto;
      position: relative;
      h2 {
        padding-bottom: 10px;
      }
      .error {
        position: absolute;
        width: 100%;
        text-align: center;
        margin-bottom: 10px;
        color: red;
        font-size: 80%;
        left: 0;
        top: 38px;
      }
      .row {
        height: 60px;
        margin-bottom: 10px;
        input {
          width: 330px;
          height: 36px;
          border: solid 1px rgba(0, 0, 0, 0.15);
          border-radius: 5px;
          font-size: 14px;
          padding-left: 10px;
        }
        .warning {
          font-size: 80%;
          padding-left: 10px;
          padding-top: 5px;
          color: red;
        }
      }
      .submit-button, .cant-submit-button {
        display: block;
        width: 330px;
        height: 40px;
        border-radius: 5px;
        font-size: 16px;
        &:hover {
          box-shadow: inset 0 1px 2px rgba(0,0,0,0.15), 0 1px 1px rgba(255,255,255,0.7);
        }
      }
      .submit-button {
        cursor: pointer;
        background-color: rgba(162, 226, 214, 0.08);
        border: solid 1px rgba(162, 226, 214, 1);
        color: #017E66; 
      }
    }
  }
}
</style>