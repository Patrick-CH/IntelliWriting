<template>
  <div class="news">
    <banner title="历史记录" />
    <div class="news-section">
      <div class="news-section-content">
        <div style="margin:20px"></div>
        <div class="content-nav-item">
          <div class="item-list" v-for='(p, index) in history'>
            <a @click="detailBtn(p)"> 
              <p class="item-list-title">{{p.title}}</p>
            </a>
            <p class="item-list-content">{{p.abstract}}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- detail ref="msgBtn"></detail -->
    <el-dialog :visible.sync="examineBtn"
            width="1000px">
    <el-form label-width="130px"
              class="item">
        <div class="invoice">
            <div class="title">文章详情</div>
            <el-form-item label="文章标题">{{ title }}</el-form-item>
            <el-form-item label="文章摘要">
              <textarea v-model="abstract" class="abs_style"
                style="border: 1px solid;border-color:#dcdfe6;padding: 10px;border-radius: 4px;overflow: auto;margin-bottom:10px"/>
            </el-form-item>
            <el-form-item label="文章内容">
              <textarea v-model="content" class="content_style"
                style="border: 1px solid;border-color:#dcdfe6;padding: 10px;border-radius: 4px;overflow: auto;margin-bottom:10px"/>            
            </el-form-item>
            <!-- 接受词云 -->   
            <el-form-item style="margin-top:5px;">
              <div style="margin-left:-100px;">
                <img :src="imgUrl" alt="" srcset="" />
              </div>
            </el-form-item>
        </div>
    </el-form>
    </el-dialog>
  </div>
</template>

<script>
import Banner from "../components/Banner";
import axios from "axios"
export default {
  data() {
    return {
      history: [],
      examineBtn: false,
      title: '',
      abstract: '',
      content: '',
      imgUrl: ''
    };
  },
  mounted(){
    var current_user = localStorage.getItem("current_user");
    if(current_user != null){
      var formData = new FormData();
      formData.append('msg', "history");
      formData.append('user', current_user);
      axios.post("api/api/history", formData).then(({ data: res }) => {      
        this.history = res.history;
      });
    } else {
      this.$message({        
        message: '请先登录',
        type: 'failure'
      });
    }
  },
  components: {
    Banner
  },
  methods: {    
    detailBtn(p) {
      window.console.log("查看详情");    
      this.examineBtn = true;
      this.title = p.title;
      this.abstract = p.abstract;
      this.content = p.content;
      this.imgUrl = "/api/api/wpic/" + p.img;
      window.console.log(this.imgUrl);
    }, 
  }
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

.item .title {
  color: #841816;
  font-size: 18px;
  font-weight: 700;
  margin: 10px 0;
  margin-left: 60px;
}
 
.invoice {
  width: 450px;
  display: inline-block;
  vertical-align: top;
}
.item .el-form-item__label {
    color: #000 !important;
    font-weight: 700 !important;
}

.abs_style{
  width: 600px;
  height: 100px;
  font-size: 14px;
  font-family: SimHei;
}
.content_style{
  width: 600px;
  height: 600px;
  font-size: 14px;
  font-family: SimHei;
}
</style>