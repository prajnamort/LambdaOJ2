<template>
	<div class="content-wrapper error-wrapper clearfix">
    <div class="miku-wrapper">
      <img class="miku" src="../../static/miku4.jpg">
    </div>
    <div class="text-wrapper">
      <div class="text">
        <div class="big-text">404</div>
        <div>你闯入了虚空之地！</div>
      </div>
    </div>
  </div>
</template>

<script>
	
</script>

<style lang="less">
.error-wrapper {
  margin-top: 80px !important;
  .miku-wrapper {
    float: left;
    height: 400px;
    .miku {
      width: 400px;
      height: auto;
    }
  }
  .text-wrapper {
    width: 484px;
    height: 350px;
    float: left;
    padding-left: 40px;
    position: relative;
    .text {
      font-size: 38px;
      color: #666;
      overflow: hidden;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      .big-text {
        font-size: 70px;
      }
    }
  }
}
</style>
