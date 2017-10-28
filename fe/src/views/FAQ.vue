<template>
  <div class="content-wrapper faq">
    <div class="caption-wrapper clearfix">
      <h1 class="title bold">LambdaOJ Helps</h1>
      <div class="info-wrapper clearfix">
        <div class="contributor clearfix">
          <span class="text small bold">by&nbsp;
            <span class="author">Kainwen</span>
          </span>  
        </div>
      </div>
    </div>
    <div class="desc desc-item">
      <div class="title bold large">提交程序须知</div>
      <div class="text">
        <ul>
        <li>程序只能从<code>stdin</code>读取数据，并输出到<code>stdout</code>, 打开文件等非法操作会使提交不正确。</li>
        <li>判题程序运行在<code>Linux</code>系统，<code>Kernel</code>版本是<code>4.4.0-96-generic</code></li>
        <li>目前支持<code>C</code>和<code>C++</code>两种语言: <br>
        <ul><li><code>C</code>: 编译器是<code>gcc</code>, 编译优化选项是<code>O2</code></li>
        <li><code>C++</code>: 编译器是<code>g++</code>, 编译优化选项是<code>O2</code></li></ul></li>
        <li>判题有如下结果: <br>
        <ul><li><code>ACCEPTED</code>: 结果完全正确</li>
        <li><code>WRONG_ANSWER</code>: 程序正常执行，也没有超时和超内存，但是答案不对</li>
        <li><code>TIME_LIMIT_EXCEEDED</code>: 程序超时，可能是死循环，也可能是算法不够优，或者实现不够优, 还没到核对答案那一步，内存情况也不明</li>
        <li><code>MEMORY_LIMIT_EXCEEDED</code>: 程序超过内存限制，可能是算法不够优，或者实现不够优，也没有到核对答案那一步</li>
        <li><code>OUTPUT_LIMIT_EXCEEDED</code>: 输出数据过多，要么程序有bug，要么是恶意代码</li>
        <li><code>BAD_SYSCALL</code>: 使用了非法的系统调用，要么是恶意代码，大部分情况是<code>C++</code>在<code>new</code>一块内存的时候，超过了限制失败了，<code>C++</code>运行时环境需要一个系统调用关闭信号，然后杀死这个进程。</li>
        <li><code>RUN_TIME_ERROR</code>:  运行时错误，可能是由于除零、引用空指针或者数组越界等等</li></ul></li>
        <li>每个测试样例的时间和内存限制都是一样的</li>
        <li>关于IO消耗的时间: <br>
        <ul><li>在测试的输入输出规模很大的时候，<code>C</code>的<code>scanf</code>和<code>printf</code>要比<code>C++</code>的<code>cin</code>和<code>cout</code>快得非常非常多</li>
        <li>如果<code>C++</code>程序加一句<code>std::ios::sync_with_stdio(false);</code>这样<code>cin</code>和<code>cout</code>就会跟<code>scanf</code>和<code>printf</code>差不多快（更快一点点）</li>
        <li>OJ统计的时间是包括IO时间的</li>
        <li>原因分析在此：<a href="https://stackoverflow.com/questions/1042110/using-scanf-in-c-programs-is-faster-than-using-cin" target="_blank">https://stackoverflow.com/questions/1042110/using-scanf-in-c-programs-is-faster-than-using-cin</a></li></ul></li>
        </ul>
      </div>
    </div>
    <div class="desc desc-item">
      <div class="title bold large">帮我们完善OJ代码</div>
      <div class="text">
        <p>OJ的代码主要分成两块:</p>
        <ul>
          <li><a href="https://github.com/kainwen/liblambdaOJ2" target="_blank">https://github.com/kainwen/liblambdaOJ2</a> (Judge)</li>
          <li><a href="https://github.com/prajnamort/LambdaOJ2" target="_blank">https://github.com/prajnamort/LambdaOJ2</a> (Web)</li>
        </ul>
        <p>帮助我们完善OJ的途径有:</p>
        <ul>
          <li>提出反馈意见 <br>
            <ul>
              <li>github issue</li>
              <li>google groups: lambdahackers@googlegroups.com</li>
            </ul>
          </li>
          <li>愿意加入、参与开发，提出Pull Request或者直接维护代码</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'faq',
  data () {
    return {
    }
  },
  computed: {
   },
  methods: {
  }
}
</script>

<style lang="less">
.faq {
  @lambdaGreen: #5cb85c;
  @lambdaGreenDarker: #55a955;
  &.content-wrapper {
    padding-bottom: 80px;
  }
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
      // padding-left: 20px;
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
        color: #666;
        .author {
          color: #666;
        }
      }
    }
  }
  .desc-item {
    &.desc {
      margin-top: 10px;
    }
    .text {
      code {
        font-size: 120%;
        padding: 0 2px;
      }
    }
  }
}
</style>
