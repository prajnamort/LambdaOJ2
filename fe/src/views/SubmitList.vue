<template>
	<div class="submit-list">
    <h2>提交历史</h2>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>分数</th>
          <th>题目</th>
          <th>语言</th>
          <th>提交时间</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="item in displayItems">
          <tr @click="goTo(item.id)">
            <td>
              <router-link :to="'/submit/' + item.id">{{ item.id }}</router-link >
            </td>
            <td>{{ item.score | scoreRange }}</td>
            <td>{{ item.problem_title }}</td>
            <td>{{ item.language }}</td>
            <td>{{ item.create_time | localtime }}</td>
          </tr>
        </template>
      </tbody>
    </table>
    <pagination :totalPage="pageNum" @goPage="getList"></pagination>
  </div>
</template>

<script>
import { getSubmitList } from '@/api/submit'
import Pagination from '@/components/pagination'

export default {
  name:'submit-list',
  components: { Pagination },
  data () {
    return {
      pageInfo: {
        page: 1,
        page_size: 50
      },
      pageNum: 0,
      displayItems: []
    }
  },
  methods: {
    getList(val) {
      this.pageInfo.page = val
      return new Promise((resolve, reject) => {
        getSubmitList(this.pageInfo.page, this.pageInfo.page_size).then(response => {
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
      this.$router.push({path: '/submit/'+ val.toString()})
    }
  },
  created() {
    this.getList(this.pageInfo.page)
  }
}
</script>

<style lang="less">
.submit-list {
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 0 auto;
    thead {
      tr {
        line-height: 40px;
        padding: 8px;
        th {
          &:first-child {
            width: 10%;
          }
          &:nth-child(2) {
            width: 10%;
          }
          &:nth-child(3) {
            width: 40%;
          }
          &:nth-child(4) {
            width: 10%;
          }
          &:last-child {
            width: 20%;
          }
        }
      }
    }
    tbody {
      tr {
        line-height: 25px;
        td {
          padding: 8px;
          text-align: center;
          &:first-child {
            width: 10%;
          }
          &:nth-child(2) {
            width: 10%;
          }
          &:nth-child(3) {
            width: 40%;
          }
          &:nth-child(4) {
            width: 10%;
          }
          &:last-child {
            width: 20%;
          }
          a {
            color: #5cb85c;
            display: block;
          }
        }
        &:nth-child(odd) {
          background-color: #f5f5f5;
        }
        &:hover {
          cursor: pointer;
          background: rgba(162, 226, 214, 0.08);
        }
      }
    }
  }
}
</style>