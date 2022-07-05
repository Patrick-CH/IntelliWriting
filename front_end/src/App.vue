<template>
  <div id="app">
    <el-container style="background-color: #841816;">
      <el-header>
        <div class="logo">
          <img src="./assets/img/toplogo.png" alt />
        </div>
        <el-menu
          text-color="#fff"
          active-text-color="#ffd04b"
          :default-active="defaultActive"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          :router="router"
        >
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item index="/news">精品时讯</el-menu-item>
          <el-menu-item index="/product">创作中心</el-menu-item>
          <el-menu-item index="/history">历史记录</el-menu-item>
          <el-menu-item index="/intro">使用说明</el-menu-item>
          <el-menu-item index="/contactus">联系我们</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <div class="footer" v-show="isShow">
        <div class="footer-content">
          <ul class="content-nav">
            <li>
              <p>推荐学习：</p>
            </li>
            <li>
              <span onclick="window.open('http://www.people.com.cn/')">人民网</span>
              <span onclick="window.open('http://www.xinhuanet.com/')">新华网</span>
              <span onclick="window.open('https://www.gmw.cn/')">光明网</span>
              <span onclick="window.open('https://www.youth.cn/')">中国青年网</span>
            </li>
            <li>
              <span onclick="window.open('http://www.china.com.cn/')">中国网</span>
              <span onclick="window.open('https://www.cctv.com/')">央视网</span>
              <span onclick="window.open('http://www.cri.cn/')">国际在线</span>
              <span onclick="window.open('http://cn.chinadaily.com.cn/')">中国日报网</span>
            </li>
            <li>
              <span onclick="window.open('http://www.cnr.cn/')">央广网</span>
              <span onclick="window.open('http://www.workercn.cn/')">中工网</span>
              <span onclick="window.open('http://www.qstheory.cn/')">求是网</span>
              <span onclick="window.open('https://www.chinanews.com.cn/')">中国新闻网</span>
            </li>
            <li>
              <span onclick="window.open('http://www.dangjian.cn/')">党建网</span>
              <span onclick="window.open('http://www.legaldaily.com.cn/')">法制网</span>
              <span onclick="window.open('http://www.ce.cn/')">中国经济网</span>
              <span onclick="window.open('http://www.gov.cn/')">中国政府网</span>
            </li>
          </ul>
          <img src="./assets/img/toplogo.png" alt />
        </div>
      </div>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      router: true,
      defaultActive: "/",
      isShow: false
    };
  },
  methods: {
    handleSelect(key) {
      this.isShow = this.defaultActive != key;
      window.console.log(this.isShow);
    }
  }
};
</script>

<style lang="scss">
* {
  padding: 0;
  margin: 0;
}
html,
body {
  height: 100%;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.el-header {
  display: flex;
  justify-content: space-between;
  align-content: center;
  width: 1240px;
  margin: 0 auto;
  background-color: #841816;

  .el-menu {
    background-color: #841816;
  }

  .logo {
    width: 80px;
    padding: -10px;
    img {
      width: 100%;
      line-height: 50px;
    }
  }
}
.el-main {
  padding: 0 !important;
}

.footer {
  width: 100%;
  height: 216px;
  overflow: hidden;
  background-color: #841816;
  &-content {
    width: 1240px;
    margin: 0 auto;
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    .content-nav {
      display: flex;
      justify-content: space-around;
      li {
        display: flex;
        flex-direction: column;
        padding: 0 20px;
        //justify-content: center;
        align-items: flex-start;
        p {
          font-size: 20px;
          color: #f7f7f7;
          padding: 7px 0;
        }
        span {
          color: #f7f7f7;
          font-weight: 300;
          padding: 10px 0;
          cursor:pointer;
        }
      }
    }
    img {
      width: 240px;
      height: 200px;
      // padding: 0px;
    }
  }
  .copyright {
    height: 30px;
    background: #841816;
    span {
      color: #fff;
      line-height: 30px;
    }
  }
}
</style>
