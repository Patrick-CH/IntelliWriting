<template>
  <div class="product">
    <banner img="../assets/img/bgtop.jpg" title="创作中心" />
    <div class="product-content" v-loading="loading">
      <div class="p-video">
        <el-row :gutter="50">
          <el-col :span="12">
            <h3 class="head">原始文本</h3>
            <el-input
              type="textarea"
              :rows="28"
              placeholder="请输入内容"
              maxlength="2000"
              show-word-limit
              style="margin-top:10px;"
              v-model="textarea">
            </el-input>
            <el-row>
              <el-popconfirm title="是否确认清除文本框内所有内容？" @confirm="clear()">
                <el-button slot="reference" type="warning" plain icon="el-icon-delete-solid" class="button1">
                  清空内容
                </el-button>
              </el-popconfirm>
              <el-upload
                action="upload"
                :http-request="handleUploadFile"
                ref="upload"
                class="upload-demo"               
                accept=".docx, .doc"
                :show-file-list="false">
                <el-button type="primary" plain icon="el-icon-upload" class="button2">导入Word</el-button>
              </el-upload>
              <el-upload
                action="upload"
                :http-request="handleUploadFile1"
                ref="upload"
                class="upload-demo"               
                accept=".png, .jpg"
                :show-file-list="false">
                <el-button type="primary" plain icon="el-icon-camera-solid" class="button2">文字识别</el-button>
              </el-upload>
              <el-button type="success" plain icon="el-icon-s-opportunity" class="button3" @click="success">
                获取
              </el-button>
            </el-row>
          </el-col> 
          <el-col :span="12">
            <h3 class="head">生成摘要</h3>
            <template>
              <div>
                <vue-slider
                  v-model="value"
                  :min="1"
                  :max="10"
                  :default="6"
                  :interval="1"
                ></vue-slider>
              </div>
            </template>
            <div style="margin-top:10px;background-color: #ffffff;">
              <!-- 接受摘要内容 -->
              <p style="border: 1px solid;border-color:#dcdfe6;padding: 10px;height: 230px;border-radius: 4px;overflow: auto;margin-bottom:10px">
                {{abstract}}
              </p>
            </div>
            <h3 class="head">生成标题</h3>
            <div style="margin-top:10px;
              border: 1px solid;
              border-color:#dcdfe6;
              background-color: #ffffff;
              padding: 10px;
              height: 50px;
              border-radius: 4px;
              overflow: auto">
                <el-row style="margin-top:15px;">
                  <!-- 接受标题内容 -->
                  <div style="width:400px; float: left" id="t1">
                    <h3>{{ title1 }}</h3>
                  </div>
                  <div style="float: left">
                    <el-link type="primary" style="float:right">复制</el-link>
                  </div>
                </el-row>
                <!-- <el-divider></el-divider> -->
            </div>
            <h3 class="head" style="margin-top:15px;">相似标题</h3>
            <div style="margin-top:10px;
              border: 1px solid;
              border-color:#dcdfe6;
              background-color: #ffffff;
              padding: 10px;
              height: 190px;
              border-radius: 4px;
              overflow: auto">
                <el-col style="margin-top:15px;">
                  <!-- 接受相似标题内容 -->
                  <div style="height:20px">
                    <div style="width:400px;">{{sim1}}</div>
                  </div>
                  <el-divider></el-divider>
                  <div style="height:20px">
                    <div style="width:400px;">{{sim2}}</div>
                  </div>
                  <el-divider></el-divider>
                  <div style="height:20px">
                    <div style="width:400px;">{{sim3}}</div>
                  </div>
                </el-col>
            </div>
          </el-col>
        </el-row>
        <!-- 接受词云 -->
        <el-row style="margin-top:5px;">
          <div style="margin-left:100px;">
            <img :src="imgUrl" alt="" srcset="" />
          </div>
        </el-row>
        <!-- 接受计时结果 -->
        <el-row style="margin-top:5px;">
          <p>{{time_consumption_text}}</p>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
  import Banner from "../components/Banner";
  import axios from "axios";
  export default {
    data() {
      return {
        textarea: '',
        title1: '', 
        abstract: '',
        value: 6,
        sim1: '',
        sim2: '',
        sim3: '',
        file: '',
        imgUrl:'',
        time_consumption_text:''
      };
    },
    components: {
      Banner
    },
    methods: {
      success() {
        // this.$message({
        //   message: '文章内容已上传成功，请耐心等待哦！',
        //   type: 'success'
        // });
        if (this.textarea.length > 0){
          var start = new Date();
          var formData = new FormData();
          formData.append('context', this.textarea);
          formData.append('num_sentence', this.value);
          formData.append('use_wordcloud', 'True');
          axios.post("api/api/title", formData).then(({ data: res }) => {    
            // 根据返回更新页面  
            this.title1 = res.title;
            this.abstract = res.abstract;
            this.sim1 = res.sim_title[0].title;
            this.sim2 = res.sim_title[1].title;
            this.sim3 = res.sim_title[2].title;
            if (res.pic.length > 0){
              this.imgUrl = "/api/api/wpic/" + res.pic;
            }
            // 计算时间
            var end = new Date();
            var time_comsumption = end.getTime() - start.getTime();
            this.time_consumption_text = `本次预测消耗时间为:  ${time_comsumption/1000.0} S`;
          });
        }
      },
      clear(){
        this.textarea = '';
        this.abstract = '';
        this.title1 = '';
        this.sim1 = '';
        this.sim2 = '';
        this.sim3 = '';
        this.imgUrl = '';
        this.time_consumption_text = '';
        window.console.log("clear!")
      },
      handleUploadFile (params) {
        // const that = this
        const _file = params.file
        var formData = new FormData();
        formData.append("file", _file);
        axios.post("api/api/file", formData).then(({ data: res }) => {
          window.console.log(res.msg);
          this.textarea = res.context;
          this.success();
        })
      },
       handleUploadFile1 (params) {
        // const that = this
        const _file = params.file
        var formData = new FormData();
        formData.append("file", _file);
        axios.post("api/api/ocr", formData).then(({ data: res }) => {
          window.console.log(res.msg);
          this.textarea = res.context;
          this.success();
        })
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

.el-upload {
  display: inline;
  text-align: center;
  cursor: pointer;
  outline: 0;
}
.upload-demo {
  display: inline;
  margin-left: 10px;
}

.button1 {
  width: 118px;
  margin-top: 10px;
}

.button2 {
  margin-top: 10px;
  margin-left: 0px;
  width: 118px;
}

.button3 {
  margin-top: 10px;
  margin-left: 10px;
  width: 90px;
}

.head {
  text-align:center;
  font-family: "YouYuan";
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 10px;
  // color: #fff;
}
</style>