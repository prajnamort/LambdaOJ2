<template>
  <div class="content-wrapper index">
    <div class="logo-wrapper">
      <img class="logo-long" src="../../static/logo_long.png">
    </div>
    <pagination :totalPage="pageNum" @goPage="getList"></pagination>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>题目</th>
          <th>通过率</th>
          <th>截止日期</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="item in displayItems">
          <tr @click="goTo(item.number)">
            <td>
              <router-link :to="'/problem/' + item.number">{{ item.number }}</router-link >
            </td>
            <td>
              <router-link :to="'/problem/' + item.number">{{ item.title }}</router-link >
            </td>
            <td>{{ acceptRate(item.accept_cnt, item.submit_cnt) }}</td>
            <td>{{ item.deadline | localtime }}</td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script>
import { getProblemList } from '@/api/problem'
import Pagination from '@/components/pagination'

export default {
  name: 'index',
  components: { Pagination },
  data () {
    return {
      msg: 'Welcome to LambdaOJ2!',
      pageInfo: {
        page: 1,
        page_size: 10
      },
      pageNum: 0,
      displayItems: []
    }
  },
  computed: {
  },
  methods: {
    acceptRate(acceptCnt, submitCnt) {
      if(submitCnt == 0) {
        return '0.00%'
      } else {
        let rate = ((acceptCnt/submitCnt)*100).toFixed(2)
        return rate.toString() + '%'
      }
    },
    getList(val) {
      this.pageInfo.page = val || 1
      return new Promise((resolve, reject) => {
        getProblemList(this.pageInfo.page, this.pageInfo.page_size).then(response => {
          const data = response.data
          console.log(data)
          this.displayItems = data.results
          this.pageNum = Math.ceil(data.count / this.pageInfo.page_size)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    goTo(val) {
      this.$router.push({path: '/problem/'+ val.toString()})
    }
  },
  // created() {
  //   this.getList()
  // }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
.index {
  .logo-wrapper {
    margin: 20px auto;
    .logo-long {
      width: 480px;
      height: auto;
      margin: 20px 220px 30px;
    }
  }
  table {
    border-collapse: collapse;
    width: 100%;
    thead {
      tr {
        line-height: 25px;
        padding: 8px;
        th {
          padding: 8px 0 8px 60px;
          text-align: left;
          &:first-child {
            width: 8%;
            padding-right: 40px;
          }
          &:nth-child(2) {
            width: 45%;
          }
          &:nth-child(3) {
            width: 12%;
          }
          &:last-child {
            width: 35%;
          }
        }
      }
    }
    tbody {
      tr {
        line-height: 25px;
        td {
          padding: 8px 0 8px 60px;
          a {
            color: #5cb85c;
            display: block;
          }
          &:first-child {
            width: 8%;
            padding-right: 40px;
          }
          &:nth-child(2) {
            width: 45%;
          }
          &:nth-child(3) {
            width: 12%;
          }
          &:last-child {
            width: 35%;
          }
        }
        &:nth-child(odd) {
          background-color: #f5f5f5;
        }
        &:hover {
          cursor: pointer;
          background: rgba(162, 226, 214, 0.08);
          // font-weight: 700;
        }
      }       
    }
  }
}
</style>
