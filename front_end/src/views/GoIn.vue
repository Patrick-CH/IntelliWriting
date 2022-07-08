<template>
  <div class="go-in">
    <banner img="../assets/img/bgtop.jpg" title="使用说明" />
    <div class="section">
      <div class="section-content">
        <div class="content-summary">
          <div class="summary-left">
            <p class="title">关于我们</p>
            <p class="eTitle">ABOUT US</p>
            <p class="content">
              赤心智能创作平台，集合领先的自然语言处理技术，拥有丰富的辅助创作功能:
            </p>
            <p class="content">              
               ·智能内容审查，告别内容风险
            </p>
            <p class="content">
               ·智能标题推荐，助你拟定标题
            </p>
            <p class="content">
               ·智能摘要生成，快速纵览全文
            </p>
            <p class="content">
               ·文字内容识别，一键上传作品
            </p>
            <p class="content">
              更懂你的智能创作助手
            </p>
          </div>
          <div class="summary-right">
            <img src="../assets/img/toplogo.png" alt />
          </div>
        </div>
        <el-divider class="el-divider-active">
          <i class="el-icon-arrow-down el-icon-arrow-down-active"></i>
        </el-divider>
        <!-- 发展历程 -->
        <div class="content-course">
          <div class="top">
            <h3>使 用 说 明</h3>
            <p>INSTRUCTION</p>
          </div>
          <!-- 待写入 加边框加样式 -->
            <p class="intro">
              赤心创作平台可以提供多个创作辅助功能，包括：自动摘要、自动标题、相似标题提示，原文输入总共由三种方式：
            </p>
            <p class="intro">
              方式一：在“原始文本”一栏中输入或者粘贴新闻文本，点击“获取标题、摘要”，即可获取自动生成的标题、摘要、相似标题。在“原始文本一栏”中输入或者粘贴新闻文本，点击“获取标题、摘要”，即可获取自动生成的标题、摘要、相似标题。
            </p>
            <p class="intro">
              方式二：点击“导入word”，可以看到选择文件的弹窗，在窗口中选择需要上传的文本文件，并点击打开。
            </p>
            <p class="intro">
              方式三：点击“文字识别”，可以看到选择文件的弹窗，在窗口中选择需要上传的图片，并点击打开。
            </p>
            <p class="intro">
              若您仍在使用上存在问题和疑惑，请及时联系我们！
            </p>
          <div>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Banner from "../components/Banner";
import { swiper, swiperSlide } from "vue-awesome-swiper";
export default {
  components: {
    Banner,
    swiper,
    swiperSlide
  },
  data() {
    return {
      loading: true,
      honorList: [],
      partnerImg: [],
      courseList: [],
      teamItem: [],
      swiperOption: {
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      },
      dialogTableVisible: false,
      dialogUrl: "",
      dialogTitle: ""
    };
  },
};
</script>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
}

.intro{
  margin: 40px;
  color: #841816;
  font-size: 20px;
  text-indent: 25px;
  line-height: 40px;
}

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

@keyframes imgboxkey {
  0% {
    border: solid rgb(29, 66, 185) 2px;
  }
  40% {
    border: solid rgb(255, 255, 255) 2px;
  }
  60% {
    border: solid rgb(255, 255, 255) 2px;
  }
  100% {
    border: solid rgb(29, 66, 185) 2px;
  }
}

@keyframes imgbo {
  0% {
    transform: scale(1);
    box-shadow: 0px 0px 0px 0px #ababab;
  }
  50% {
    transform: scale(1.1);
    box-shadow: 0px 0px 10px 5px #ababab;
  }
  100% {
    transform: scale(1);
    box-shadow: 0px 0px 0px 0px #ababab;
  }
}
.el-divider--horizontal {
  margin: 1px 0;
}

.top {
  h3,
  p {
    text-align: center;
    color: #3c6088;
    font-weight: 400;
    padding: 10px 0;
  }
  h3 {
    font-size: 30px;
  }
  p {
    font-size: 20px;
  }
  .border {
    border-bottom: 1px solid #3c6088;
    width: 15%;
    margin: 0 auto;
  }
}
// .swiper-button-disabled {
//   display: none;
// }
.order {
  order: -1;
}
.order-top {
  order: 1;
}
.el-divider {
  background-color: red;
  height: 3px;
  .el-divider__text {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    padding: 0px;
    color: #fff;
    border: 3px solid red;
  }
}
.el-divider-active {
  background-color: #841816;
}
.honor-big-img {
  width: 100%;
  height: 100%;
  z-index: 10;
  text-align: center;
  padding-bottom: 20px;
  padding: 5%;
  //background-color: #14679f;
  .el-dialog__wrapper {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    overflow: auto;
    margin: 0;

    .el-dialog__body {
      overflow: hidden;
      img {
        width: 100%;
      }
    }
  }
}
</style>