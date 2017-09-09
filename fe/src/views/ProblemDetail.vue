<template>
  <div class="content-wrapper problem-detail">
    <h1 class="title bold">{{ detail.title }}</h1>
    <div class="contributor clearfix">
      <img class="avatar" src="../../static/BLUE.png">
      <span class="text small bold">by {{ detail.contributor }}</span>
    </div>
    <div class="desc" v-html="detail.desc"></div>
    <div class="input_desc">
      <div class="title bold">Input Format</div>
      <div class="text" v-html="detail.input_desc"></div>
    </div>
    <div class="output_desc">
      <div class="title bold">Output Format</div>
      <div class="text" v-html="detail.output_desc"></div>
    </div>
    <div class="input_sample">
      <div class="title bold">Input Sample</div>
      <pre class="text" v-html="detail.input_sample"></pre>
    </div>
    <div class="output_sample">
      <div class="title bold">Output Sample</div>
      <pre class="text" v-html="detail.output_sample"></pre>
    </div>
    <div v-if="detail.hint" class="hint">
      <div class="title bold">Hint</div>
      <div class="text" v-html="detail.hint"></div>
    </div>
    <div class="submit-wrapper">
      <div class="title-wrapper clearfix">
        <div class="title bold">Your Code</div>
        <div class="dropmenu">
          <select v-model="selectedLanguage">
            <option v-for="language in languages">
              {{ language }}
            </option>
          </select>
        </div>
      </div>
      <textarea placeholder="Please copy your code here..." v-model="code"></textarea>
      <button @click="submitCode">Submit Code</button>
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
  padding: 20px;
  .title {
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .contributor {
    height: 25px;
    line-height: 25px;
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
  .desc {
    margin-top: 20px;
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
    margin-top: 30px;
    .title-wrapper {
      .title {
        line-height: 52px;
        margin: 0;
        float: left;
      }
      .dropmenu {
        line-height: 52px;
        float: right;
      }
    }
    textarea {
      width: 100%;
      height: 200px;
    }
  }
}
</style>
