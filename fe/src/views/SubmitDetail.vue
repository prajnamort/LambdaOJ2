<template>
	<div class="content-wrapper submit-detail">
    <h2 class="bold">提交详情（
      <router-link :to="'/problem/' + detail.problem" class="problem-title">
        <span class="bold">{{ detail.problem_title }}</span>
      </router-link> ）
    </h2>
    <div class="subtitle-wrapper clearfix">
      <div class="username">
        <span class="title">提交者: </span>
        <span class="text">{{ detail.user_username }}</span>
      </div>
      <div class="create-time">
        <span class="title">创建时间: </span>
        <span class="text">{{ detail.create_time | localtime }}</span>
      </div>
    </div>
    <template v-if="loading">
      <div class="judge-status">
        <div class="title bold">Judge Status</div>
        <div class="text">{{ detail.judge_status }}</div>
      </div>
      <div class="states">
      </div>
    </template>
    <template v-else>
      <template v-if="compileSuccess">
      <div class="result-wrapper">
        <div class="result-title-wrapper clearfix">
          <div class="left-title bold">运行结果</div>
          <div class="score clearfix">
            <div class="right-title bold">分数</div>
            <div class="text">{{ detail.score | toFixedTwo }}</div>
          </div>
        </div>        
        <div class="run-results">           
          <table>
            <thead>
              <tr>
                <th>#</th>
                <th>状态</th>
                <th>时间</th>
                <th>内存</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in detail.run_results">
                <td>{{ index + 1 }}</td>
                <td>
                  <!-- <span class="bold" :class="getColorType(item[0])">{{ item[0] | sampleStatus }}</span> -->
                  <span class="bold" :class="getColorRandom()">{{ item[0] | sampleStatus }}</span>
                </td>
                <td>{{ item[1] | milliseconds }}</td>
                <td>{{ item[2] }} KB</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      </template>
      <template v-else>
        <div v-if="detail.error_message" class="error-message">
          <span class="title bold large">编译失败</span>
          <pre>{{ detail.error_message }}</pre>
        </div>
      </template>
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
      poll: null,
      id: 0,
      test: false
    }
  },
  computed: {
    loading() {
      return (this.detail.judge_status !== 'C')
    },
    compileSuccess() {
      return (this.detail.compile_status === 'O')
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
    getColorType(val) {
      let color = ""
      switch(val) {
        case 0:
          color = "green"
          break
        case 1:
        case 5:
        case 6:
        case 7:
          color = "red"
          break
        case 2:
        case 3:
        case 4:
          color = "orange"
          break
        default:
          break
      }
      return color
    },
    getColorRandom() {
      let val = Math.floor(Math.random() * 3)
      let color = ""
      switch(val) {
        case 0:
          color = "green"
          break
        case 1:
          color = "red"
          break
        case 2:
          color = "orange"
          break
        default:
          break
      }
      return color
    },
    // waitForJudge(id, resolve, reject) {
    //   // const endTime = Number(new Date()) + 50000
    //   getSubmitDetail(id).then(response => {
    //     const data = response.data
    //     this.detail = data
    //     console.log(this.detail)
    //     if(this.detail.judge_status === 'C') {
    //       // this.test = true
    //       return resolve();
    //     }
    //     // console.log(Number(new Date()) < endTime)
    //     // setTimeout(this.waitForJudge(id, resolve, reject), 1000)
    //     // else if(Number(new Date()) < endTime) {
    //     //   setTimeout(this.waitForJudge(id, resolve, reject), 1000)
    //     // } else {
    //     //   return reject(new Error('timed out'))
    //     // }
    //   })
    // },
    pollDetail(id) {
      const endTime = Number(new Date()) + 50000

      this.poll = setInterval(() => {
        getSubmitDetail(id).then(response => {
          const data = response.data
          this.detail = data
          console.log(this.detail)
          if(this.detail.judge_status === 'C') {
            clearInterval(this.poll)
          }
          else if (Number(new Date()) > endTime) {
            clearInterval(this.poll)
            console.log('time out')
          }
        })
      }, 1000)
    }
  },
  created() {
    this.id = this.$route.params.id
    this.getDetail(this.id)
    this.pollDetail(this.id)
  }
}
</script>

<style lang="less">
.submit-detail {
  @lamdbaGreen: #5cb85c;
  @lamdbaGreenDarker: #55a955;
  padding: 20px;
  .problem-title {
    color: @lamdbaGreen;
    &:hover {
      color: @lamdbaGreenDarker;
    }
    &:visited {
      color: @lamdbaGreen;
      &:hover {
        color: @lamdbaGreenDarker;
      }
    }
  }
  .subtitle-wrapper {
    padding-top: 10px;
    .username {
      float: left;
      padding-right: 40px;
    }
    .create-time {
      float: left;
    }
    .username, .create-time {
      .text {
        height: 22px;
        line-height: 22px;
        margin-left: 5px;
        padding: 0 10px;
        background-color: #f5f5f5;
        color: rgba(0, 0, 0, 0.4);
        border-radius: 10px;
        font-weight: 600;
      }
    }
  }
  .title {
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .result-wrapper {
    width: 790px;
    margin: 30px auto 40px;
    padding: 20px 0 50px;
    // border: 1px solid #aaa;
    background: rgba(162, 226, 214, 0.08);
    border-radius: 10px;
    .result-title-wrapper {
      height: 52px;
      line-height: 52px;
      width: 720px;
      margin: 0 auto;
      .left-title {
        float: left;
      }
      .score {
        float: right;
        .right-title {
          float: left;
          padding-right: 20px;
        }
        .text {
          float: right;
        }
      }
    }
    .run-results {
      table {
        border-collapse: collapse;
        width: 720px;
        text-align: center;
        margin: 0 auto;
        thead {
          tr {
            line-height: 25px;
            padding: 8px;
            th {
              padding: 8px 6px;
              &:first-child {
                padding-left: 20px;
                width: 10%;
              }
              &:nth-child(2) {
                width: 40%;
              }
              &:nth-child(3) {
                width: 25%;
              }
              &:last-child {
                width: 25%;
              }
            }
          }
        }
        tbody {
          tr {
            line-height: 25px;
            td {
              padding: 8px 6px;
              // border-bottom: 1px solid #ddd;
              &:first-child {
                padding-left: 20px;
                width: 10%;
              }
              &:nth-child(2) {
                width: 40%;
              }
              &:nth-child(3) {
                width: 25%;
              }
              &:last-child {
                width: 25%;
              }
              .green,
              .red,
              .orange {
                color: white;
                padding: 2px 10px;
                border-radius: 13px;
              }
              .green {
                background-color: @lamdbaGreen;
              }
              .red {
                background-color: #ff5555;
              }
              .orange {
                background-color: #ff9a47;
              }
            }
            &:nth-child(odd) {
              background-color: #f5f5f5;
            }
            &:nth-child(even) {
              background-color: white;
            }
          }       
        }
      }
    }
  }
  .error-message {
    margin-top: 20px;
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