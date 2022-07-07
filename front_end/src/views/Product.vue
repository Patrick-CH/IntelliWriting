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
              <el-popconfirm title="是否确认清除文本框内所有内容？" @confirm="clear()">
                <el-button slot="reference" type="warning" round plain icon="el-icon-delete-solid" style="margin-top:10px;margin-right:10px">
                  清空
                </el-button>
              </el-popconfirm>
              <el-button type="success" round plain icon="el-icon-s-opportunity" @click="success">
                获取标题、摘要
              </el-button>
            </el-row>
            <el-row style="margin-top:10px">
              <!-- 导入Word -->
              <el-upload
                action="upload"
                :http-request="handleUploadFile"
                ref="upload"               
                accept=".docx, .doc"
                :show-file-list="false">
                <el-button type="primary" round plain icon="el-icon-upload">导入Word</el-button>
              </el-upload>
              <!-- OCR识别 -->
              <el-upload
                action="upload"
                :http-request="handleUploadFile1"
                ref="upload"               
                accept=".png, .jpg"
                :show-file-list="false">
                <el-button type="primary" round plain icon="el-icon-camera-solid">文字识别</el-button>
              </el-upload>
            </el-row>
          </el-col> 
          <el-col :span="12">
            <h3 style="text-align:center">生成摘要</h3>
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
            <h3 style="text-align:center">生成标题</h3>
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
                  <div style="width:400px; float: left" id="t1">{{ title1 }}</div>
                  <div style="float: left">
                    <el-link type="primary" style="float:right">复制</el-link>
                  </div>
                </el-row>
                <!-- <el-divider></el-divider> -->
            </div>
            <h3 style="text-align:center;margin-top:15px;">相似标题</h3>
            <div style="margin-top:10px;
              border: 1px solid;
              border-color:#dcdfe6;
              background-color: #ffffff;
              padding: 10px;
              height: 80px;
              border-radius: 4px;
              overflow: auto">
                <el-row style="margin-top:15px;">
                  <!-- 接受相似标题内容 -->
                  <div style="width:400px; float: left">{{sim1}}</div>
                  <div style="width:400px; float: left">{{sim2}}</div>
                  <div style="width:400px; float: left">{{sim3}}</div>
                </el-row>
                <!-- <el-divider></el-divider> -->
            </div>
          </el-col>
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
        file: ''
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
        var formData = new FormData();
        formData.append('context', this.textarea);
        formData.append('num_sentence', this.value);
        axios.post("api/api/title", formData).then(({ data: res }) => {      
          this.title1 = res.title;
          this.abstract = res.abstract;
          this.sim1 = res.sim_title[0].title
          this.sim2 = res.sim_title[1].title
          this.sim3 = res.sim_title[2].title
        });
        // window.console.log(this.value);
      },
      clear(){
        this.textarea = '';
        this.abstract = '';
        this.title1 = '';
        this.sim1 = '';
        this.sim2 = '';
        this.sim3 = '';
        window.console.log("clear!")
      },
      handleUploadFile (params) {
        // const that = this
        const _file = params.file
        var formData = new FormData();
        formData.append("file", _file);
        window.console.log(_file.name);
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
        window.console.log(_file.name);
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
</style>