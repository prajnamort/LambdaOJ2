<template>
  <div class="personal-info">
    <h2>Personal Information</h2>
    <template v-if="curUser">
      <div class="username">
        <span class="title">Username: </span>
        <span>{{ curUser.username }}</span>
      </div>
      <div v-if="curUser.student_id" class="student-id">
        <span class="title">Student ID: </span>
        <span>{{ curUser.student_id }}</span>
      </div>
      <div v-if="curUser.mobile" class="mobile">
        <span class="title">Mobile: </span>
        <span>{{ curUser.mobile }}</span>
      </div>
      <div class="email">
        <span class="title">Email: </span>
        <span>{{ curUser.email }}</span>
      </div>
      <div>
        <router-link :to="'/account'">修改密码</router-link>
      </div>
    </template>
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
          console.log(this.curUser)
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

}
</style>