<template>
  <div class="go-in">
    <banner img="../assets/img/bgtop.jpg" title="用户中心" />
    <div class="p-video">
      <el-row :gutter="50">
      <el-col :span="10" id="left_box">
        <h3 class="head">登录</h3>
        <el-row>
          <el-input v-model="username_login" placeholder="用户名" class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-input v-model="password_login" placeholder="密码" show-password class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-button type="primary" @click="login" class="login_style">登录</el-button>
        </el-row>
      </el-col>
      <el-col :span="1">
        <div class="verticalBar"></div>
      </el-col>
      <el-col :span="10">
        <h3 class="head">注册</h3>
        <el-row>
          <el-input v-model="username_reg" placeholder="用户名" class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-input v-model="email" placeholder="邮箱" class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-input v-model="password_reg" placeholder="密码" show-password class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-input v-model="password_reg_con" placeholder="确认密码" show-password class="input_style"></el-input>
        </el-row>
        <el-row>
          <el-button type="primary" @click="sign_up" class="login_style">注册</el-button>
        </el-row>      
      </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Banner from "../components/Banner";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import axios from "axios";
export default {
  components: {
    Banner,
    swiper,
    swiperSlide
  },
  data() {
    return {
      username_login: '',
      password_login: '',
      username_reg: '',
      email: '',
      password_reg: '',
      password_reg_con: '',
    };
  },
  methods:{
    login(){
      var start = new Date();
      var formData = new FormData();
      formData.append('name', this.username_login);
      formData.append('passwd', this.password_login);
      axios.post("/api/users/login", formData).then(({ data: res }) => {    
        if(res["success"]){
          // 登录成功
          localStorage.setItem('current_user', this.username_login);
          this.$message({        
            message: `登录成功，欢迎用户 ${localStorage.getItem('current_user')} `,
            type: 'success'
          });
        } else {
          this.$message({        
            message: '登录失败',
            type: 'failure'
          });
        }
      });
    },
    sign_up(){
      if(this.password_reg == this.password_reg_con){
        var start = new Date();
        var formData = new FormData();
        formData.append('name', this.username_reg);
        formData.append('passwd', this.password_reg);
        formData.append('email', this.email);
        axios.post("/api/users/register", formData).then(({ data: res }) => {    
          if(res["success"]){
            // 注册成功
            localStorage.setItem('current_user', this.username_reg);
            this.$message({        
              message: `注册成功，欢迎用户 ${localStorage.getItem('current_user')} `,
              type: 'success'
            });
          } else {
            this.$message({        
              message: '用户名已被占用',
              type: 'failure'
            });
          }
        });
      } else {
        // 两次输入不一致
        this.$message({        
          message: '请确保两次密码输入一致',
          type: 'failure'
        });
      }     
    },
  }
};
</script>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
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


.p-video {
  width: 1000px;
  margin: 0 auto;
  padding: 60px 0;
  background-color: #ffffff;
}

.input_style{
width: 200px;
height: 50px;
margin-bottom: 20px;
margin-left:150px;
font-size: 40;
}
.login_style{
width: 200px;
height: 30px;
margin-bottom: 20px;
margin-left: 150px;
}
.head{
margin-left:230px;
margin-bottom:20px;
}

#left_box{
margin-top: 60px;
}

.verticalBar {
  width: 2px;
  height: 300px;
  background: #D3D3D3;
  display: inline-block;
  margin-top: 30px;
  vertical-align: top;
  margin-left: 63px;
}

</style>