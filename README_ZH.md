[**English**](README.md) | [**中文说明**](README_ZH.md)

# IntelliWriting

IntelliWriting 是一个基于改进版TextRank的智能写作工具，可以智能生成标题和摘要。



## 介绍

标题预测、摘要预测一直是NLP领域中的一个重要任务，依据文本特性的不同，研究者和算法工程师们提出了各种各样的算法来预测标题和介绍。其中，[TextRank](https://aclanthology.org/W04-3252.pdf) 由Google用于搜索引擎的 [PageRank](https://en.wikipedia.org/wiki/PageRank) 改进而来，是一个重要的文本摘要算法。本项目对TextRank进行了一定程度的改进，不仅实现了对摘要的计算，也成功预测了标题，在学习强国的新闻数据中测试结果达到了 Rouge-L 19.3% 的效果。



### 概要

项目结构


Project Structure

```file tree
.
├── back_end
│   ├── app.py
│   ├── forms.py
│   ├── get_abstract.py
│   ├── get_title.py
│   ├── ReinforcedTextRank
│   ├── requirements.txt
│   ├── start_service.sh
│   ├── static
│   ├── templates
│   └── test.py
├── front_end
│   ├── babel.config.js
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   ├── README.md
│   ├── src
│   └── vue.config.js
├── README.md
├── README_ZH.md
├── ReinforcedTextRank
└── train
    ├── app.py
    ├── config
    ├── data_helper.py
    ├── data_set.py
    ├── generate_title.py
    ├── http_server.py
    ├── model.py
    ├── README.md
    ├── requirements.txt
    ├── runs
    ├── templates
    ├── test_gpt.py
    ├── train.py
    └── vocab
```

部分重要文件和作用如下
- back_end    项目后端
  - app.py	使用flask 提供网络服务
  - ReinforcedTextRank   使用知识增强改进后的TextRank算法实现
- front_end   项目后端
- train       GPT2模型训练代码



### 特性

我们使用由TextRank改进而来的ReTextRank，能够快速计算出标题和摘要，在测试集合上，平均 0.1s 内就能计算出一篇新闻的标题和摘要。



### 测试结果

我们使用了学习强国的新闻数据进行测试，测试效果如下：

| 测试指标 | Rouge-1 | Rouge-2 | Rouge-L |
| -------- | ------- | ------- | ------- |
| 测试结果 | 32.2    | 20.3    | 19.3    |



## 安装和使用

您可以按照以下步骤安装我们的系统：

1.下载：

```shell
git clone https://github.com/Patrick-CH/IntelliWriting.git
```

2.运行后端

```shell
cd ./IntelliWriting/back_end
sudo chmod u+x start_service.sh
sudo ./start_service.sh
```

3.运行前端

```shell
./IntelliWriting/front_end
sudo chmod u+x start_service.sh
sudo ./start_service.sh
```

4.使用

调用API，获取测试结果，假设 app.py 正在localhost:9000上运行，API使用示例代码如下:

```javascript
var form = new FormData();
form.append("context", "全面建设社会主义现代化国家新征程已经开启，第二个百年奋斗目标就在前方。");

var settings = {
 "url": "http://localhost:9000/api/title",
 "method": "POST",
 "timeout": 0,
 "processData": false,
 "mimeType": "multipart/form-data",
 "contentType": false,
 "data": form
};

$.ajax(settings).done(function (response) {
 console.log(response);
});
```



## 开发

我们的系统提供网页和API服务

接口定义：

| 方法 | 路径       | form-data               | response                                      |
| :--- | :--------- | :---------------------- | :-------------------------------------------- |
| POST | /api/title | {“context”：“示例文章”} | {“title”：“示例标题”, "abstract": "实例摘要"} |
| GET  | /          |                         | 测试界面                                      |



## 版本日志

V0：我们第一个验证系统框架的版本。

V1：首次发布功能比较丰富的版本。



## 分支

- Product (master ): 稳定版本
- Develop (dev branch): 最新版本
- Feature : 添加新的特性 (仍在开发中)
- Release : 公开发行版 (仍在开发中)



## 参考

[1]  Mihalcea R, Tarau P. TextRank: Bringing order into texts[C]. Association for Computational Linguistics, 2004.

[2]  [TextRank4ZH](https://github.com/letiantian/TextRank4ZH): 中文 TextRank 的 Python3 实现



### 联系我们

如果您有任何问题或建议，请随时通过 yukechen_patrick@foxmail.com 给我们发送电子邮件。



## 作者和致谢

作者：

- 来自武汉理工大学的 陈禹轲
- 来自武汉理工大学的 沈明轩
- 来自武汉理工大学的 余孜卓



我们要感谢武汉理工大学为我们提供了一个合作的机会。

我们要感谢武汉理工大学的教授，李琳老师，激发了我们对创新技术发展的兴趣。