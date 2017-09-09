<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <router-link class="logo" to="/" exact>
          首页
        </router-link>
        <div class="nav-items">
          <template v-if="is_login">
            <router-link class="nav-item" to="/profile">个人中心</router-link>
            <span class="nav-item" @click="logout">退出</span>
          </template>
          <template v-else> 
            <router-link class="nav-item" to="/login">登录</router-link>
          </template>
        </div>
      </nav>
    </header>
    <router-view :key="key"></router-view>
  </div>
</template>

<script>
import { getToken } from '@/utils/auth' // 验权

export default {
  name: 'app',
  computed: {
    key() {
      return this.$route.name !== undefined ? this.$route.name + +new Date() : this.$route + +new Date()
    },
    is_login() {
      if(this.$store.getters.auth_token) {
        return true
      }
      return false
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('LogOut').then(() => {
        this.$router.push({ path: '/' })
        location.reload()// 为了重新实例化vue-router对象 避免bug
      })
    }
  }
}
</script>

<style lang="less">
@bodyBgColor: #F4F3F1;
body {
  padding: 0;
  margin: 0;
}
* {
  box-sizing: border-box;
}
a {
  text-decoration: none;
  &:hover {
    text-decoration: none;
  }
}
.clearfix::after {
  content: '';
  display: block;
  width: 0;
  height: 0;
  clear: both;
}
.bold {
  font-weight: 600;
}
.small {
  font-size: 90%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  header {
    @headerHeight: 50px;
    @bgColor: rgba(162, 226, 214, 0.08);
    @textColor: #017E66;
    width: 100%;
    height: @headerHeight;
    background-color: rgba(162, 226, 214, 0.08);
    .inner {
      width: 960px;
      margin: 0 auto;
      .logo {
        color: @textColor;
        width: 60px;
        text-align: center;
        line-height: @headerHeight;
        float: left;
      }
      .nav-items {
        float: right;
        margin-right: 10px;
        .nav-item{
          color: @textColor;
          display: inline-block;
          padding: 0 10px;
          line-height: 50px;
          &:hover {
            cursor: pointer;
            font-weight: 700;
          }
        }
      }
    }
  }
  .content-wrapper {
    @media only screen and (max-width : 960px) {
        min-width: 960px;
    }
    max-width: 960px;
    margin: 0 auto 50px;
    padding: 20px;
    // font-family: '微软雅黑', 'Microsoft Yahei', arial;
    // background-color: @bodyBgColor;
  }
}
</style>
