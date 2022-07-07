<template>
  <div class="news">
    <banner title="历史记录" />
    <div class="news-section">
      <div class="news-section-content">
        <div style="margin:20px"></div>
        <div class="content-nav-item">
          <div class="item-list" >
            <p class="item-list-title">习近平回信勉励种粮大户 带动广大小农户多种粮种好粮 一起为国家粮食安全贡献力量</p>
            <p class="item-list-content">新华社北京6月28日电 中共中央总书记、国家主席、中央军委主席习近平6月27日给安徽省太和县的种粮大户徐淙祥回信，向当地的乡亲们表示问候，对全国的种粮大户提出殷切期望。
            习近平在回信中说，我记得你这个安徽太和的种粮能手。得知你家种植的小麦喜获丰收，儿孙也跟着你干起了农业，我感到很高兴。
            习近平指出，手中有粮，心中不慌。对粮食生产，我一直都很关注，基层调研时也经常到田间地头看一看。这些年，党中央出台了一系列支持粮食生产的政策举措，就是要让中国人的饭碗牢牢端在自己手中，就是要让种粮农民有钱挣、得实惠，日子越过越好。
            </p>
          </div>
          <div class="item-list">
            <p class="item-list-title">习近平主持全球发展高层对话会并发表重要讲话</p>
            <p class="item-list-content">新华社北京6月24日电 国家主席习近平24日晚在北京以视频方式主持全球发展高层对话会并发表重要讲话。阿尔及利
              亚总统特本、阿根廷总统费尔南德斯、埃及总统塞西、印度尼西亚总统佐科、伊朗总统莱希、哈萨克斯坦总统托卡耶夫、俄罗斯总统普京、塞内加尔总统
              萨勒、南非总统拉马福萨、乌兹别克斯坦总统米尔济约耶夫、巴西副总统莫朗、柬埔寨首相洪森、埃塞俄比亚总理阿比、斐济总理姆拜尼马拉马、印度总
              理莫迪、马来西亚总理伊斯迈尔、泰国总理巴育出席。各国领导人围绕“构建新时代全球发展伙伴关系，携手落实2030年可持续发展议程”的主
              题，就加强国际发展合作、加快落实联合国2030年可持续发展议程等重大问题深入交换意见，共商发展合作大计，达成广泛重要共识。            
            </p>
          </div>
          <div class="item-list">
            <p class="item-list-title">金砖国家领导人第十四次会晤举行 习近平主持会晤并发表重要讲话</p>
            <p class="item-list-content">新华社北京6月23日电 国家主席习近平23日晚在北京以视频方式主持金砖国家领导人第十四次会晤。南非总统拉马福
              萨、巴西总统博索纳罗、俄罗斯总统普京、印度总理莫迪出席。人民大会堂东大厅花团锦簇，金砖五国国旗整齐排列，与金砖标识交相辉映。
              晚8时许，金砖五国领导人集体“云合影”，会晤开始。            
            </p>
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
};
</script>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
}
.news {
  width: 100%;
  height: 100%;
  background-color: #841816;
  position: relative;
  overflow: hidden;

  &-section {
    width: 100%;
    //height: 1600px;

    &-content {
      width: 1240px;
      //height: 1600px;
      margin: 0 auto;
      background-color: #fff;
      border: 1px solid red;

      .content-nav {
        width: 400px;
        height: 55px;
        margin: 0 auto;
        display: flex;
        //justify-content: center;
        align-items: center;
        position: relative;
        bottom: 30px;
        border: 1px solid red;

        &-btn {
          width: 50%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
          background-color: #e4e4e4;
          transition: all 0.2s;
        }

        .content-nav-active {
          background-color: red;
          color: #fff;
        }
      }

      .category{
        margin-top:20px;
        margin-left:95px;
        font: 20px sans-serif;
        text-align:center;
        line-height:40px;
        color:#ffffff;
        width: 100px;
        height: 40px;
        background-color: #d0021b;
        border: #d0021b 0px solid;
        border-radius: 5px;
        box-shadow: 5px 5px 5px grey;
      }

      .content-nav-item {
        width: 1100px;
        margin: 0 auto;
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        //border: 1px solid blue;

        .item-list {
          width: 1100px;
          height: 150px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          margin: 10px 10px;
          border: 1px solid #841816;
          border-radius: 10px;

          &:hover {
            border: 1px solid #fff;
            box-shadow: 0 0 5px 2px #897575;
            cursor:pointer;
          }
          .item-img {
            width: 320px;
            height: 210px;
            background-color: #cecece;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            background-origin: content-box;
            border: #fff 0px solid;
            border-radius:5px ;
          }

          &-title {
            width: 1000px;
            height: 40px;
            color: #d30000;
            font-size: 22px;
            padding: 0 10px;
            margin: 20px 0;
            overflow: hidden;
            text-overflow: ellipsis;
            border-left: 5px solid #d30000;
          }

          &-content {
            width: 1000px;
            height: 110px;
            font-size: 14px;
            color: gray;

            // 文本长度处理 begin
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 5;
            -webkit-box-orient: vertical;
            white-space: normal !important;
            word-wrap: break-word;
            // 文本长度处理 ending
          }

          &-more {
            width: 273px;
            padding-top: 20px;
            display: flex;
            justify-content: flex-start;
            align-items: center;

            img {
              width: 12px;
              height: 12px;
            }
            span {
              color: #e13834;
              padding: 0 5px;
            }
          }
        }
      }
    }
  }
  .text-decoration {
    text-decoration: none;
  }
}
</style>