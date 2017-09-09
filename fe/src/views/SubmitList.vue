<template>
	<div class="submit-list">
    <h2>Submit History</h2>
    <table>
      <thead>
        <tr>
          <th>Submit</th>
          <th>Score</th>
          <th>Problem</th>
          <th>Language</th>
          <th>Submit Time</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="item in displayItems">
          <tr>
            <td>
              <router-link :to="'/submit/' + item.id">{{ item.id }}</router-link >
            </td>
            <td>{{ item.score }}</td>
            <td>
              <router-link :to="'/problem/' + item.problem">{{ item.problem }}</router-link >
            </td>
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
    thead {
      tr {
        line-height: 40px;
        padding: 8px;
        th {
          width: 20%;
        }
      }
    }
    tbody {
      tr {
        line-height: 25px;
        td {
          width: 20%;
          padding: 8px;
          text-align: center;
          border-bottom: 1px solid #ddd;
          a {
            display: block;
          }
        }
        &:hover {
          background: rgba(0, 0, 0, 0.05);
          font-weight: 700;
        }
      }
    }
  }
}
</style>