<template>
  <div class="personal-info">
    <h2>账号信息</h2>
    <div class="info-wrapper">
      <template v-if="curUser">
        <div class="username item clearfix">
          <div class="title">账号: </div>
          <div class="text">{{ curUser.username }}</div>
        </div>
        <div v-if="curUser.student_id" class="student-id item clearfix">
          <div class="title">学号: </div>
          <div class="text">{{ curUser.student_id }}</div>
        </div>
        <div v-if="curUser.mobile" class="mobile item clearfix">
          <div class="title">手机: </div>
          <div class="text">{{ curUser.mobile }}</div>
        </div>
        <div  v-if="curUser.email" class="email item clearfix">
          <div class="title">邮箱: </div>
          <div class="text">{{ curUser.email }}</div>
        </div>
        <div class="password item clearfix">
          <div class="title">密码: </div>
          <div class="text">*******</div>
          <router-link class="link" :to="'/account'">修改密码</router-link>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'personal-info',
  data() {
    return {
      curUser: {},
    }
  },
  methods: {
    getCurUser() {
      if(this.$store.getters.username) {
        this.curUser = this.$store.getters.user
      } else {
        this.$store.dispatch('GetUserInfo').then(() => {
          this.curUser = this.$store.getters.user
        }).catch(() => {
          // this.loading = false
          this.curUser = {}
        })
      }
    }
  },
  created() {
    this.getCurUser()
  }
}
</script>

<style lang="less">
.personal-info {
  @lamdbaGreen: #5cb85c;
  @lamdbaGreenDarker: #55a955;
  .info-wrapper {
    padding-left: 20px;
    .item {
      height: 30px;
      line-height: 30px;
      .title {
        float: left;
        width: 60px;
      }
      .text {
        float: left;
      }
      .link {
        display: block;
        float: left;
        padding-left: 20px;
        color: @lamdbaGreen;
        &:hover {
          color: @lamdbaGreenDarker;
        }
      }
    }
  }

}
</style>