<template>
	<div class="content-wrapper submit-detail">
    <router-link :to="'/problem/' + detail.problem">
      <h2 class="bold">{{ detail.problem_title }}</h2>
    </router-link>
    <div class="time">
      <span class="title">Submit Time: </span>
      <span>{{ detail.create_time | localtime }}</span>
    </div>
    <div class="judge_status">
      <div class="title bold">Judge Status</div>
      <div class="text">{{ detail.judge_status }}</div>
    </div>
    <template v-if="loading">
      <div class="states">
        Judging...Please wait :)
      </div>
    </template>
    <template v-else>
      <div class="score">
        <div class="title bold">Score</div>
        <div class="text">{{ detail.score }}</div>
      </div>
      <div class="compile_status">
        <div class="title bold">Compile Status</div>
        <div class="text">{{ detail.compile_status }}</div>
      </div>
      <div class="run_results">
        <div class="title bold">Run Results</div>
        <div class="text">{{ detail.run_results }}</div>
      </div>
    </template>
    <div class="code">
      <div class="title bold">Code</div>
      <template v-if="detail.code">
        <pre v-highlightjs><code class="content cpp">{{ detail.code }}</code></pre>
      </template>
    </div>
	</div>
</template>

<script>
import { getSubmitDetail } from '@/api/submit'

export default {
  name: 'submit-detail',
  data () {
    return {
      detail: {},
      problemDetail: {},
      id: 0,
      test: false
    }
  },
  computed: {
    loading() {
      if (this.detail.judge_status === 'C') {
        return false
      }
      return true
    }
  },
  methods: {
    getDetail(id) {
      return new Promise((resolve, reject) => {
        getSubmitDetail(id).then(response => {
          const data = response.data
          this.detail = data
          console.log(this.detail)
          // this.getProblemTitle(this.detail.problem)
          resolve()
        }).then(() => {
          // if(this.loading) {
          //   pollDetail(id)
          // }
        }).catch(error => {
          reject(error)
        })
      })
    },
    getProblemTitle(number) {
      return new Promise((resolve, reject) => {
        getProblemDetail(number).then(response => {
          const data = response.data
          this.problemDetail = data
          console.log(this.problemDetail)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    checkTest() {
      setTimeout(this.showTest, 2000)
    },
    showTest() {
      console.log(this.test)
      this.test = true
    },
    waitForJudge(id, resolve, reject) {
      const endTime = Number(new Date()) + 50000
      console.log(endTime)
      getSubmitDetail(id).then(response => {
        const data = response.data
        this.detail = data
        console.log(this.detail)
        if(this.detail.judge_status === 'C') {
          // this.test = true
          return resolve();
        } 
        // console.log(Number(new Date()) < endTime)
        // setTimeout(this.waitForJudge(id, resolve, reject), 1000)
        // else if(Number(new Date()) < endTime) {
        //   setTimeout(this.waitForJudge(id, resolve, reject), 1000)
        // } else {
        //   return reject(new Error('timed out'))
        // }
      })
    },
    pollDetail(id) {
      return new Promise((resolve, reject) => {
        this.waitForJudge(id, resolve, reject)
      })
    }
  },
  created() {
    // this.showTest()
    this.id = this.$route.params.id
    this.getDetail(this.id)
    this.pollDetail(this.id)
    // this.checkTest()
  }
}
</script>

<style lang="less">
.submit-detail {
  padding: 20px;
  .title {
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .code {
    .content {
      display: block;
      width: 100%;
      font-size: 14px;
      border-radius: 5px;
      padding: 10px;
    }
  }
}
</style>