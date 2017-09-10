<template>
  <div class="content-wrapper login">
    <div class="logo-wrapper">
      <img class="logo-long" src="../../static/logo_long.png">
    </div>
    <div class="login-form-wrapper">
      <div class="error" v-show="!correct">用户名或密码错误</div>
      <form class="login-form" :model="loginForm" v-on:submit.prevent="handleLogin">
        <div class="row">
          <input v-validate="'required'" name="username" type="text" v-model.trim="loginForm.username" placeholder="用户名"/>
          <div class="warning" v-if="errors.has('username')">{{ errors.first('username') }}</div>
        </div>
        <div class="row">
          <input v-validate="'required'" name="password" type="password" v-model.trim="loginForm.password" placeholder="密码"/>
          <div class="warning" v-if="errors.has('password')">{{ errors.first('password') }}</div>
        </div>
        <input class="submit-button" type="submit" value="登录"/>
      <!-- 
        <div class="row form-group">
          <input class="form__input" name="password" type="password" @keyup.enter.native="handleLogin" v-model="loginForm.password" placeholder="密码" @input="$v.loginForm.password.$touch()"/>
          <template v-if="$v.loginForm.password.$error">
            <div class="form-group__message warning" v-if="!$v.loginForm.password.required">请输入密码</div>
          </template>
        </div>
        <template v-if="canSubmit">
          <input class="submit-button" type="submit" value="登录"/>
        </template>
        <template v-else>
          <span class="cant-submit-button">登录</span>
        </template> -->
      </form>
    </div>
  </div>
</template>

<script>
import { Validator } from 'vee-validate'

const dict = {
  en: {
    custom: {
      username: {
        required: '请输入用户名' // messages can be strings as well.
      },
      password: {
        required: '请输入密码' // messages can be strings as well.
      }
    }
  }
}
Validator.updateDictionary(dict)

export default {
  name: 'login',
  data () {
    return {
      correct: true,
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    handleLogin() {
      this.$store.dispatch('LoginByUsername', this.loginForm).then(() => {
        if(this.$route.query.redirect) {
          let url = decodeURIComponent(this.$route.query.redirect)
          this.$router.push({path: url})
        }
        else { 
          this.$router.push({ path: '/' })
        }
      }).catch((error) => {
        // this.loading = false
        console.log(error.response)
        if(error.response.status == 400) {
          this.correct = false
        }
      })
    }
  }
}
</script>

<style lang="less">
.login {
  .logo-wrapper {
    margin: 20px auto;
    .logo-long {
      width: 300px;
      height: auto;
      margin: 20px 305px 0px;
    }
  }
  .login-form-wrapper {
    padding-top: 20px;
    position: relative;
    .login-form {
      width: 330px;
      margin: 0 auto;
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
      .cant-submit-button {
        text-align: center;
        line-height: 40px;
        cursor: not-allowed;
        background-color: #F4F3F1;
        border: solid 1px rgba(0,0,0,0.15);
        color: rgba(0,0,0,0.15); 
      }
    }
  }
}
</style>
