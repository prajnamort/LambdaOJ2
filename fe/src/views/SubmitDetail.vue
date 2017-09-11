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
    <template v-if="judging">
      <div class="loading-wrapper clearfix">
        <div class="miku-wrapper">
          <img class="miku" src="../../static/miku.gif">
        </div>
        <div class="judge-text">
          Miku 正在判题中...
        </div>
      </div>
      <div class="states">
      </div>
    </template>
    <template v-else-if="pending">
      <div class="loading-wrapper clearfix">
        <div class="miku-wrapper">
          <img class="miku" src="../../static/miku2.gif">
        </div>
        <div class="judge-text">
          Miku 正在赶来帮你判题...
        </div>
      </div>
      <div class="states">
      </div>
    </template>
    <template v-else-if="failed">
      <div class="loading-wrapper clearfix">
        <div class="miku-wrapper">
          <img class="miku" src="../../static/miku3.jpg">
        </div>
        <div class="judge-text">
          判题失败了...
        </div>
      </div>
      <div class="states">
      </div>
    </template>
    <template v-else>
      <template v-if="compileSuccess">
      <div class="empty-result-wrapper" v-if="isEmptyResults(detail.run_results)">
        <div class="loading-wrapper clearfix">
          <div class="miku-wrapper">
            <img class="miku" src="../../static/miku3.jpg">
          </div>
          <div class="judge-text">
            没有测试样例, 无法判题...
          </div>
        </div>
      </div>
      <div class="result-wrapper" v-else>
        <div class="result-title-wrapper clearfix">
          <div class="left-title bold">运行结果</div>
          <div class="score clearfix">
            <div class="right-title bold">分数</div>
            <div class="text">{{ detail.score | scoreDisplay }}</div>
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
                  <span class="bold" :class="getColorType(item[0])">{{ item[0] | sampleStatus }}</span>
                </td>
                <template v-if="isAccept(item[0])">
                  <td>{{ item[1] | milliseconds }}</td>
                  <td>{{ item[2] }} KB</td>
                </template>
                <template v-else>
                  <td>-</td>
                  <td>-</td>
                </template>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      </template>
      <template v-else>
        <div v-if="detail.error_message" class="error-message">
          <span class="title bold large">Compilation Error</span>
          <div class="message-wrapper">
            <pre>{{ detail.error_message }}</pre>
          </div>
        </div>
      </template>
    </template>
    <div class="code">
      <div class="caption-wrapper clearfix">
        <div class="title bold">Code</div>
        <div class="language small">{{ detail.language }}</div>
      </div>
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
      id: 0
    }
  },
  computed: {
    judging() {
      return (this.detail.judge_status === 'J')
    },
    pending() {
      return (this.detail.judge_status === 'P')
    },
    failed() {
      return (this.detail.judge_status === 'F')
    },
    loading() {
      return (this.judging || this.pending)
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
          if(this.detail.judge_status !== 'C' && 
             this.detail.judge_status !== 'F') {
            this.pollDetail(id)
          }
          resolve()
        }).then(() => {
        }).catch(error => {
          reject(error)
        })
      })
    },
    isAccept(item) {
      return (item === 0)
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
    isEmptyResults(results) {
      return !Boolean(results.length)
    },
    pollDetail(id) {
      const duration = 3600 * 1000
      const endTime = Number(new Date()) + duration

      this.poll = setInterval(() => {
        getSubmitDetail(id).then(response => {
          const data = response.data
          this.detail = data
          if(this.detail.judge_status === 'C' || 
             this.detail.judge_status === 'F') {
            clearInterval(this.poll)
          }
          else if (Number(new Date()) > endTime) {
            clearInterval(this.poll)
            console.log('time out')
          }
        }).catch(error => {
          clearInterval(this.poll)
        })
      }, 1000)
    }
  },
  created() {
    this.id = this.$route.params.id
    this.getDetail(this.id)
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
  .loading-wrapper {
    margin: 60px 0 30px;
    .miku-wrapper {
      float: left;
      height: 350px;
    }
    .judge-text {
      width: 484px;
      float: left;
      height: 350px;
      line-height: 350px;
      font-size: 38px;
      padding-left: 30px;
      color: #35767A;
      overflow: hidden;
    }
  }
  .title {
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .result-wrapper {
    width: 790px;
    margin: 40px auto 30px;
    padding: 20px 0 50px;
    // border: 1px solid #aaa;
    background: rgba(162, 226, 214, 0.08);
    border-radius: 10px;
    border: 2px solid #BAE8BA;
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
    .title {
      display: block;
    }
    .message-wrapper {
      background: #fdf6e3;
      padding: 0 10px;
      border-radius: 5px;
      max-height: 300px;
      overflow-y: auto;
      overflow-x: hidden;
    }
  }
  .code {
    .title {
      float: left;
    }
    .language {
      margin: 20px 10px 10px;
      float: left;
      padding: 0 10px;
      height: 22px;
      line-height: 22px;
      background-color: #f5f5f5;
      color: rgba(0, 0, 0, 0.4);
      border-radius: 10px;
      font-weight: 600;
      text-align: center;
    }
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