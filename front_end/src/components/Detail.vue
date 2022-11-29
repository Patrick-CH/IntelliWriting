<template>
    <div class="wrapper">
        <div id="msgbox">
            <el-dialog :visible.sync="examineBtn"
                       width="1000px">
                <el-form label-width="130px"
                         class="item">
                    <div class="invoice">
                        <div class="title">文章详情</div>
                        <el-form-item label="文章标题"><p v-model="title"></p></el-form-item>
                        <el-form-item label="文章摘要"><p v-model="abstract"></p></el-form-item>
                        <el-form-item label="文章内容"><p v-model="content"></p></el-form-item>
                    </div>
                </el-form>
            </el-dialog>
        </div>
    </div>
</template>
<script>
export default {
    components: {},
    data() {
        return {
            form: {},
            examineBtn: false,
        };
    },
    methods: {
        init() {
            window.console.log("这是详情组件");
            var p = localStorage.getItem("p");
            window.console.log(p);
            this.examineBtn = true;
            this.title = p.title;
            this.abstract = p.abstract;
            this.content = p.content;
        },
    },
};
</script>
<style lang="scss">
 
.item .title {
  color: #1ec6df;
  font-size: 18px;
  font-weight: 700;
  margin: 10px 0;
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
</style>