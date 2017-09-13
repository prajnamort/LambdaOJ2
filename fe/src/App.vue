<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <router-link to="/" exact>
          <img class="logo" src="../static/logo.png">
        </router-link>
        <span class="nav-item-left" @click="refreshIndex()">首页</span>
        <div class="nav-items">
          <template v-if="is_login">
            <a class="nav-item" :href="adminUrl" v-if="is_staff" target="_blank">管理中心</a>
            <span class="nav-item" @click="refreshProfile()" to="/profile">个人中心</span>
            <span class="nav-item" @click="logout">退出</span>
          </template>
          <template v-else> 
            <router-link class="nav-item" to="/login">登录</router-link>
          </template>
        </div>
      </nav>
    </header>
    <router-view :key="key"></router-view>
    <footer>
      <span>Copyright © 2017 LambdaHackers.</span>
      <a href="mailto:lambdahackers@googlegroups.com">Contact us.</a>
    </footer>
  </div>
</template>

<script>
import { getToken } from '@/utils/auth' // 验权

export default {
  name: 'app',
  data () {
    return {
      adminUrl: __ADMIN__
    }
  },
  computed: {
    key() {
      return this.$route.name !== undefined ? this.$route.name + +new Date() : this.$route + +new Date()
    },
    is_login() {
      if(this.$store.getters.auth_token) {
        return true
      }
      return false
    },
    is_staff() {
      if(typeof this.$store.getters.is_staff === "object") {
        this.$store.dispatch('GetUserInfo').then(() => {
          if(this.$store.getters.is_staff) {
            return true
          }
          return false
        }).catch(() => {
          return false
        })
      }
      return this.$store.getters.is_staff
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('LogOut').then(() => {
        this.$router.push({ path: '/' })
        location.reload()// 为了重新实例化vue-router对象 避免bug
      })
    },
    refreshIndex() {
      if(this.$route.path === '/') {
        location.reload()
      } else {
        this.$router.push({ path: '/' })
      }
    },
    refreshProfile() {
      if(this.$route.path === '/profile') {
        location.reload()
      } else {
        this.$router.push({ path: '/profile' })
      }
    }
  }
}
</script>

<style lang="less">
@contentWidth: 960px;
html, body {
  padding: 0;
  margin: 0;
  height: 100%;
}
* {
  box-sizing: border-box;
}
a {
  text-decoration: none;
  color: #5cb85c;
  &:hover {
    text-decoration: none;
    color: #55a955;
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
.large {
  font-size: 110%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100%;
  position: relative;
  header {
    @headerHeight: 60px;
    @bgColor: #39424e;
    // @textColor: #C2C7D0;
    @textColor: rgba(255, 255, 255, 0.8);
    width: 100%;
    height: @headerHeight;
    background-color: @bgColor;
    .inner {
      width: 920px;
      margin: 0 auto;
      .logo {
        color: @textColor;
        width: 40px;
        height: 40px;
        text-align: center;
        line-height: @headerHeight;
        margin-top: 10px;
        float: left;
        &:hover {
          cursor: pointer;
          font-weight: 700;
        }
      }
      .nav-item-left {
        color: @textColor;
        display: inline-block;
        height: @headerHeight;
        padding-left: 20px;
        line-height: @headerHeight;
        &:hover {
          cursor: pointer;
          font-weight: 700;
        }
      }
      .nav-items {
        float: right;
        height: @headerHeight;
        line-height: @headerHeight;
        .nav-item{
          color: @textColor;
          display: inline-block;
          padding-left: 20px;
          text-align: right;
          height: @headerHeight;
          line-height: @headerHeight;
          .icon {
            display: flex;
            float: left;
            vertical-align: middle;
            align-items: center;
            justify-content: center;
            height: 50px;
            width: 30px;
            // padding-top: 16px;
          }
          &:hover {
            cursor: pointer;
            font-weight: 700;
          }
        }
      }
    }
  }
  footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 30px;
    text-align: center;
    font-size: 80%;
    color: #666;
  }
  .content-wrapper {
    @media only screen and (max-width : @contentWidth) {
        min-width: @contentWidth;
    }
    max-width: @contentWidth;
    margin: 0 auto;
    padding: 20px;
    font-family: '微软雅黑', 'Microsoft Yahei', 'Avenir', Helvetica, Arial, sans-serif;
  }
}
</style>
