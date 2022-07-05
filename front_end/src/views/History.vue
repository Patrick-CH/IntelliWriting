<template>
  <div class="case">
    <banner title="历史记录" />
    <div class="case-section" v-loading="loading">
      <div class="case-section-content">
        <img class="history" src="../assets/img/history.png" />
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
.history{
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-origin: content-box;
  border: #fff 0px solid;
  border-radius:5px ;
}
.case {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  background-color: #841816;

  &-section {
    width: 100%;
    &-content {
      width: 1240px;
      min-height: 1000px;
      margin: 0 auto;
      background-color: #fff;

      &-list {
        width: 100%;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid pink;

        img {
          width: 612px;
          height: 314px;
        }
        .content-list-abstract {
          width: 290px;
          height: 350px;
          padding: 0 20px;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          .abstract-title {
            line-height: 30px;
            font-size: 22px;
            color: #e13834;
          }
          .abstract-content {
            height: 150px;
            color: #484848;
            font-size: 15px;

            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 7;
            -webkit-box-orient: vertical;
            white-space: normal !important;
            word-wrap: break-word;
            //border: 1px solid pink;
          }
          .more {
            display: flex;
            justify-content: flex-start;
            .text-decoration {
              text-decoration: none;

              span {
                color: #000;
              }
              img {
                width: 12px;
                height: 12px;
              }
            }
          }
        }
        .abstract-active {
          order: -1;
        }
      }
    }
  }
}
</style>