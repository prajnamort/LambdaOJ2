<template>
  <div class="content-wrapper index">
    <h1>{{ msg }}</h1>
    <pagination :totalPage="pageNum" @goPage="getList"></pagination>
    <table>
      <thead>
        <tr>
          <th>Problem</th>
          <th>Title</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="item in displayItems">
          <tr>
            <td>
              <router-link :to="'/problem/' + item.number">{{ item.number }}</router-link >
            </td>
            <td>
              <router-link :to="'/problem/' + item.number">{{ item.title }}</router-link >
            </td>
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
    getList(val) {
      this.pageInfo.page = val
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
    }
  },
  created() {
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
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
h1, h2 {
  font-weight: normal;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
table {
  border-collapse: collapse;
  width: 100%;
  tbody {
    tr {
      .problem-item {
        display: block;
        width: 100%;
      }
      &:hover {
        background: rgba(0, 0, 0, 0.05);
        font-weight: 700;
      }
    }       
  }
  td {
    a {
      display: block;
    }
  }
}

th, td {
  padding: 8px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}
td:first-child,th:first-child {
  width: 20%;
}
td:last-child,th:last-child {
  width: 80%;
}
</style>
