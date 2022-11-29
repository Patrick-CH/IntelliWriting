<template>
  <div class="go-in">
    <banner img="../assets/img/appDown.jpg" title="联系我们" />
    <div class="section">
      <div class="section-content">
        <div class="content-summary">
          <div class="summary-left">
            <p class="title">欢迎来信，您的意见对我们来说非常宝贵！</p>
            <p class="eTitle">Welcome to write, your opinion is very valuable to us!</p>
            <el-input
              type="textarea"
              :rows="10"
              placeholder="请输入您的宝贵意见！"
              maxlength="1000"
              show-word-limit
              style="margin-top:10px;"
              v-model="textarea">
            </el-input>
            <el-row style="margin-top:20px;margin-left:480px">
              <el-button type="primary" plain icon="el-icon-phone" @click="success">提交意见</el-button>
            </el-row>
          </div>
          <div class="summary-right">
            <img src="../assets/img/toplogo.png" alt />
          </div>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
import Banner from "../components/Banner";
export default {
  components: {
    Banner
  },
  data() {
    return {
      textarea: ''
    }
  },
  methods: {
    success() {
      var user = localStorage.getItem("current_user");
      this.$message({        
        message: user + '您的意见已收到，我们会认真阅读，感谢您的来信！',
        type: 'success'
      });
    },
  }
};
</script>

<style lang="scss" scoped>
.go-in {
  width: 100%;
  height: 100%;
  // background-color: #14679f;
  background-color: #841816;
  position: relative;
  overflow: hidden;
  .section {
    width: 100%;
    &-content {
      width: 1240px;
      margin: 0 auto;
      background-color: #fff;

      .content-summary {
        //height: 500px;
        display: flex;
        justify-content: space-around;
        padding: 100px 0;
        .summary-left {
          width: 600px;
          .title {
            font-size: 30px;
            color: #e13834;
          }
          .eTitle {
            font-size: 20px;
            color: #e13834;
            padding: 20px 0;
          }
          .content {
            color: #14679f;
            font-size: 25px;
            text-indent: 25px;
            line-height: 40px;
          }
        }

        .summary-right {
          width: 400px;
          height: 310px;
          // border: 2px solid #1d42b9;
          //animation: imgboxkey 4s infinite;
          border-radius: 10px;
          margin-top: 80px;
          text-align: center;

          img {
            width: 360px;
            height: 270px;
            margin-top: 20px;
            //animation: imgbo 4s infinite;
          }
        }
      }

      .content-course {
        padding: 50px 0;
        .course-time {
          width: 1000px;
          height: 400px;
          margin: 20px auto;
          .swiper-container {
            height: 100%;
          }
          .time-show {
            width: 700px;
            height: 100%;
            margin: 0 auto;
            display: flex;
            .time-show-item {
              width: 350px;
              height: 100%;
              overflow: hidden;
              display: flex;
              flex-direction: column;

              .item-top,
              .item-bottom {
                height: 190px;
              }
              .item-bottom {
                // display: flex;
                // align-content: center;
                .item-bottom-content {
                  background-color: #1667a0;
                  margin: 20px 0;
                  p {
                    color: #fff;
                    text-align: center;
                    padding: 15px;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>