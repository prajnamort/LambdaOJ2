<template>
  <div class="pagination-wrapper" v-if="totalPage > 1">
    <div class="pagination clearfix">
      <span v-if="showPrev" class="page-item" @click="go(currentPage - 1)"><</span>
      <span v-else class="page-item unable"><</span>
      <template v-for="page in pages">
        <span class="page-item" :class="{'active': currentPage == page}" @click="go(page)">
          {{ page }}
        </span>
      </template>
      <span v-if="showNext" class="page-item" @click="go(currentPage + 1)">></span>
      <span v-else class="page-item unable">></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    totalPage: { // 总页数
        type: Number,
        default: 1,
        required: true
    }
  },
  data() {
    return {
      currentPage: 0,
      jumpPage: 0
    }
  },
  created () {
    this.currentPage = 1
    // if(this.mode == 'params' && !this.routeName) {
    //   throw 'need a route name when choose params mode in pager component'
    // }
  },
  computed: {
    pages () {
      let getPages = (start,end) => {
          if(start < 1 || start > end || start >= this.totalPage) {
              start = 1
          }
          if(end > this.totalPage || end < start || end < 1) {
              end = this.totalPage
          }
          let arr = []
          for(let i = start; i <= end; i++) {
              arr.push(i)
          }
          return arr
      }
      return getPages(1, this.totalPage)
    },
    showPrev() {
      return this.currentPage != 1
    },
    showNext() {
      return this.currentPage != this.totalPage
    }
  },
  methods: {
    go (page) {
      this.currentPage = parseInt(page, 10)
    }
  },
  watch: {
    currentPage(val) {
      this.$emit('goPage', val);
    }
  }
}
</script>

<style lang="less" scoped>
.pagination-wrapper {
  text-align: center;
  margin: 30px 0 20px;
  .pagination {
    clear: both;
    display: inline-block;
    .page-item {
      display: block;
      float: left;
      min-width: 33px;
      height: 30px;
      margin: 0 5px;
      border: 1px solid #C2C7D0;
      text-align: center;
      line-height: 30px;
      border-radius: 10%;
      &.active {
        background: #2ec866;
        border: 1px solid #13A853;
        color: white;
      }
      &.unable {
        color: rgba(0, 0, 0, 0.15);
        cursor: not-allowed;
        &:hover {
          cursor: not-allowed;
          box-shadow: none;
        }
      }
      &:hover {
        cursor: pointer;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.15), 0 1px 1px rgba(255,255,255,0.7);
      }
    }
  }
}
</style>