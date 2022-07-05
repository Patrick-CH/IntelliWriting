<template>
  <div class="product">
    <banner img="../assets/img/bgtop.jpg" title="创作中心" />
    <div class="product-content" v-loading="loading">
      <div class="p-video">
        <el-row :gutter="40">
          <el-col :span="10">
            <h3 style="text-align:center">原始文本</h3>
            <el-input
              type="textarea"
              :rows="20"
              placeholder="请输入内容"
              maxlength="2000"
              show-word-limit
              style="margin-top:10px;"
              v-model="textarea">
            </el-input>
            <el-row>
              <el-popconfirm
                title="是否确认清除文本框内所有内容？"
              >
                <el-button slot="reference" type="warning" round plain icon="el-icon-delete-solid" style="margin-top:10px;margin-right:10px">
                  清空
                </el-button>
              </el-popconfirm>
              <!-- OCR识别，Methods里加click事件 -->
              <el-button type="primary" round plain icon="el-icon-camera-solid">OCR识别</el-button>
              <!-- 导入Word，Methods里加click事件 -->
              <el-button type="primary" round plain icon="el-icon-upload">导入Word</el-button>
            </el-row>
            <el-row style="margin-top:10px">
              <el-button type="success" round plain icon="el-icon-s-opportunity" @click="success">获取标题</el-button>
            </el-row>
          </el-col> 
          <el-col :span="12">
            <h3 style="text-align:center">生成摘要</h3>
            <div style="margin-top:10px;background-color: #ffffff;">
              <!-- 接受摘要内容 -->
              <p style="border: 1px solid;border-color:#dcdfe6;padding: 10px;height: 230px;border-radius: 4px;overflow: auto;margin-bottom:10px">
                每个人都不可避免的一件事，就是走过青春，而青春是一个人一生之中几乎最灿烂的时光，青春的酣畅和肆意，便是往后的时光中回味，也是异常羡慕的，
                而美好的时光总是短暂的，青春成了记忆中定格的美好，能够反复回忆却无法追寻。同样的，青春时光里会留下的，除了那些美好张扬，还有青涩和遗憾，
                而这些有时候又影响了一个人的以后，那些未曾抓在手里过的，也是真正叫人念念不忘的。青春时代是一个短暂的美梦，当你醒来时，这早已消失得无影
                无踪了。你瞧，青春就在懵懵懂懂里过去了，短暂的就像是一场梦，真的能够深刻意识到青春里的美好的时候，它如烟般消散，留下的只是一段鲜艳的记忆，
                一张张熟悉的脸孔也不复旧日模样。只有这变化里，才能够找到些许残存的青春岁月。珍惜，是一件很难的事情，难的不是珍惜这件事，而是如何分辨正确
                的方法。就像执行规则可能只是按部就班，但是制定规则却要考虑到方方面面，这其中的悖论就是很多事，没有办法求全，也就是说再如何完美的事，深究
                起来总是会有遗憾。也许，有些事就如同青春一样，带着些许遗憾才算一场圆满。
              </p>
            </div>
            <h3 style="text-align:center">生成标题</h3>
            <div style="margin-top:10px;
              border: 1px solid;
              border-color:#dcdfe6;
              background-color: #ffffff;
              padding: 10px;
              height: 195px;
              border-radius: 4px;
              overflow: auto">
                <el-row style="margin-top:15px;">
                  <!-- 接受摘要内容 -->
                  <div style="width:400px; float: left">青春是一个短暂的美梦, 当你醒来时, 它早已消失无踪</div>
                  <div style="float: left">
                    <el-link type="primary" style="margin-left:10px">复制</el-link>
                  </div>
                </el-row>
                <el-divider></el-divider>
                <el-row style="margin-top:15px;">
                  <!-- 接受摘要内容 -->
                  <div style="width:400px; float: left">青春是一个美梦, 当你醒来时, 它早已消失无踪</div>
                  <div style="float: left">
                    <el-link type="primary" style="margin-left:10px">复制</el-link>
                  </div>
                </el-row>
                <el-divider></el-divider>
                <el-row style="margin-top:15px;">
                  <!-- 接受摘要内容 -->
                  <div style="width:400px; float: left">青春是一个短暂的美梦, 梦醒时分, 烟消云散</div>
                  <div style="float: left">
                    <el-link type="primary" style="margin-left:10px">复制</el-link>
                  </div>
                </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
  import Banner from "../components/Banner"; 
  export default {
    data() {
      return {
        textarea: ''
      };
    },
    components: {
      Banner
    },
    methods: {
      success() {
        this.$message({
          message: '文章内容已上传成功，请耐心等待哦！',
          type: 'success'
        });
      },
    }
  };
</script>

<style lang="scss" scoped>
.product {
  width: 100%;
  height: 100%;
  background-color: #841816;
}

.product-content {
  width: 1240px;
  margin: 0 auto;
  background-color: #fff;
}

.p-video {
  width: 1000px;
  margin: 0 auto;
  padding: 60px 0;
}

//公共样式
.title,
.eTitle {
  font-size: 34px;
  font-weight: 400;
  color: #333;
  text-align: center;
}
.eTitle {
  font-size: 30px;
  padding: 10px 0;
}
</style>