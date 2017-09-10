<template>
  <div class="content-wrapper problem-detail">
    <div class="caption-wrapper clearfix">
      <h1 class="title bold">{{ detail.title }}</h1>
      <div class="info-wrapper clearfix">
        <div class="contributor clearfix">
          <img class="avatar" src="../../static/BLUE.png">
          <template v-if="detail.contributor">
            <span class="text small bold">by {{ detail.contributor }}</span>  
          </template>
          <template v-else>
            <span class="text small bold">by 一位不愿意透露姓名的老师</span>  
          </template>
        </div>
        <div class="limit-wrapper small">
          <div class="time-limit item">
            <span class="limit_label">时间限制: </span>
            <span class="limit_content">{{ detail.time_limit | milliseconds }} </span>
          </div>
          <div class="memory-limit item">
            <span class="limit_label">内存限制: </span>
            <span class="limit_content">{{ detail.memory_limit }} KB</span>
          </div>
        </div>
      </div>
    </div>
    <div class="desc">
      <div class="title bold">问题描述</div>
      <div class="text" v-html="detail.desc"></div>
    </div>
    <div v-if="detail.input_desc" class="input_desc">
      <div class="title bold">输入格式</div>
      <div class="text" v-html="detail.input_desc"></div>
    </div>
    <div v-if="detail.output_desc" class="output_desc">
      <div class="title bold">输出格式</div>
      <div class="text" v-html="detail.output_desc"></div>
    </div>
    <div v-if="detail.input_sample" class="input_sample">
      <div class="title bold">输入样例</div>
      <pre class="text" v-html="detail.input_sample"></pre>
    </div>
    <div v-if="detail.output_sample" class="output_sample">
      <div class="title bold">输出样例</div>
      <pre class="text" v-html="detail.output_sample"></pre>
    </div>
    <div v-if="detail.hint" class="hint">
      <div class="title bold">提示</div>
      <div class="text" v-html="detail.hint"></div>
    </div>
    <div class="submit-wrapper clearfix">
      <div class="title-wrapper">
        <div class="title bold">请输入你的代码: </div>
        <div class="radios clearfix">
          <template v-for="language in languages">
            <div class="lang-item">
              <label :for="language">
                <input type="radio" :id="language" :value="language" v-model="selectedLanguage">
                <span class="content">{{ language }}</span>
                <div class="check"></div>
              </label>
            </div>
          </template>
        </div>
      </div>
      <textarea placeholder="Please paste your code here..." v-model="code"></textarea>
      <span class="submitButton" @click="submitCode">提交代码</span>
    </div>
  </div>
</template>

<script>
import { getProblemDetail } from '@/api/problem'
import { submitProblem } from '@/api/submit'

export default {
  name: 'problem-detail',
  data () {
    return {
      detail: {},
      problemNum: 0,
      submitId: '',
      languages: ['C++03', 'C++11', 'C89', 'C99', 'C11'],
      selectedLanguage: 'C++03',
      code:''
    }
  },
  computed: {
   },
  methods: {
    getDetail(number) {
      return new Promise((resolve, reject) => {
        getProblemDetail(number).then(response => {
          const data = response.data
          this.detail = data
          console.log(this.detail)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    submitCode() {
      return new Promise((resolve, reject) => {
        submitProblem(this.problemNum,
                      this.selectedLanguage,
                      this.code).then(response => {
          const data = response.data
          this.submitId = data.id
          this.$router.push({ path: '/submit/' + this.submitId })
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    }
  },
  created() {
    // console.log(this.$route.params.number);
    this.problemNum = this.$route.params.number
    this.getDetail(this.problemNum)
  }
}
</script>

<style lang="less">
.problem-detail {
  @lamdbaGreen: #5cb85c;
  @lamdbaGreenDarker: #55a955;
  padding: 20px;
    .title {
      padding-top: 20px;
      padding-bottom: 10px;
      margin: 0;
      span {
        font-size: 110%;
      }
    }
    .info-wrapper {
      height: 25px;
      line-height: 25px;
      .contributor {
        
        float: left;
        .avatar {
          float: left;
          width: 25px;
          height: 25px;
          border-radius: 5px;
          margin-right: 10px;
        }
        .text {
          display: block;
          float: left;
          line-height: 25px;
        }
      }
      .limit-wrapper {
        float: right;
        .item {
          padding-bottom: 6px;
          &.time-limit {
            float: left;
            margin-right: 20px;
          }
          &.memory-limit {
            float: right;
          }
          .limit_content {
            margin-left: 5px;
            padding: 0 10px;
            background-color: @lamdbaGreen;
            color: white;
            border-radius: 10px;
            font-weight: 600;
          }
        }
      }
    }
  .desc {
    margin-top: 10px;
  }
  .input_sample, .output_sample {
    .text {
      border-radius: 2px;
      font-size: 14px;
      padding: 20px;
      background-color: #f4faff;
      line-height: 20px;
      white-space: pre-wrap;
      color: #454c59;
    }
  }
  .submit-wrapper {
    margin: 30px auto 0;
    .title-wrapper {
      .title {
        margin: 0;
      }
      .radios {
        height: 35px;
        line-height: 35px;
        margin-bottom: 10px;
        position: relative;
        .lang-item {
          padding-right: 40px;
          float: left;
          position: relative;
          label {
            color: #666;
            position: relative;
            padding-left: 20px;
            transition: color .25s linear;
            -webkit-transition: color .25s linear;
            input[type=radio]{
              position: absolute;
              visibility: hidden;
              &:checked ~ .check {
                border: 1px solid @lamdbaGreen;
              }
              &:checked ~ .check::before{
                background: @lamdbaGreen;
              }
              &:checked ~ .content{
                color: @lamdbaGreen;
              }
            }
            .check{
              display: block;
              position: absolute;
              border: 1px solid #666;
              border-radius: 100%;
              height: 15px;
              width: 15px;
              top: 3.5px;
              left: 0px;
              z-index: 5;
              transition: border .25s linear;
              -webkit-transition: border .25s linear;
              &::before {
                display: block;
                position: absolute;
                content: '';
                border-radius: 50%;
                height: 5px;
                width: 5px;
                top: 4px;
                left: 4px;
                margin: auto;
              }
            }
            &:hover {
              cursor: pointer;
              color: rgba(0, 0, 0, 0.25);
              .check {
                border: 1px solid rgba(0, 0, 0, 0.25);
              }
            }
          }
        }
      }
    }
    textarea {
      font-size: 14px;
      width: 100%;
      height: 200px;
      resize: none;
      border: 1px solid #AAA;
      padding: 8px 10px;
    }
    .submitButton {
      float: right;
      width: 100px;
      text-align: center;
      height: 40px;
      line-height: 40px;
      background-color: @lamdbaGreen;
      color: white;
      border-radius: 5px;
      margin-top: 10px;
      transition: all .25s ease-in-out;
      &:hover {
        cursor: pointer;
        background-color: @lamdbaGreenDarker;
      }
    }
  }
}
</style>
