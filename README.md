[**English**](README.md) | [**中文说明**](README_ZH.md)

# IntelliWriting

IntelliWriting is an intelligent writing tool based on an improved version of TextRank that intelligently generates titles and abstract.



## Introduction

Title prediction has always been an important task in the field of NLP. According to the different characteristics of text, researchers and algorithm engineers have proposed a variety of algorithms to predict the title and abstract. Among them, [TextRank](https://aclanthology.org/W04-3252.pdf) , improved from Google's [PageRank](https://en.wikipedia.org/wiki/PageRank), is an important text summarization algorithm. In this project, TextRank is improved to a certain extent. Not only the summary calculation is realized, but also the title prediction is successfully achieved. The test results in the news data from [Xuexiqiangguo](https://www.xuexi.cn/) reach 19.3% rouge-L effect.

### Abstract

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

some important files and their functions are as follows
- back_end    back end of the project
  - app.py	Use Flask to provide Internet service
  - ReinforcedTextRank   Improved TextRank algorithm package using knowledge enhancement
- front_end   front end of the project
- train       code to train the GPT2 model




### Features

We use ReTextRank, an improvement of TextRank, to quickly calculate the headline and summary. On the test set, we could calculate the headline and summary of a news story in an average of 0.1s.



### Test

We use the news data from [Xuexiqinagguo](https://www.xuexi.cn/)：

| Test   | Rouge-1 | Rouge-2 | Rouge-L |
| ------ |---------|---------| ------- |
| result | 32.2    | 20.3    | 19.3    |



## Install & Use

You can install through following steps:

1.download the code

```shell
git clone https://github.com/Patrick-CH/IntelliWriting.git
```

2.run the back end

```shell
cd ./IntelliWriting/back_end
sudo chmod u+x start_service.sh
sudo ./start_service.sh
```

3.run the front_end

```shell
cd ./IntelliWriting/front_end
sudo chmod u+x start_service.sh
sudo ./start_service.sh
```

4.visit the web page
open localhost:8080, you can see the page.

5.use the API
Call the API to get the test results, assuming app.py is running on localhost:9000.

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



## Development

Our system provides web pages and API services.

Interface definition:

| method | path       | form-data               | response                                      |
| :----- | :--------- | :---------------------- | :-------------------------------------------- |
| POST   | /api/title | {“context”：“示例文章”} | {“title”：“示例标题”, "abstract": "实例摘要"} |
| GET    | /          |                         | test page                                     |



## Versions

V0: We were the first to validate the version of the system framework.

V1: This is the first release with rich functions.



## Branches

- Product (master): indicates a stable version
- Develop (Dev Branch): indicates the latest version

- Feature: Added new features (still under development)

- Release: public Release (still in development)



## Reference

[1]  Mihalcea R, Tarau P. TextRank: Bringing order into texts[C]. Association for Computational Linguistics, 2004.

[2]  [TextRank4ZH](https://github.com/letiantian/TextRank4ZH): Python3 implement of TextRank in Chinese



### Contact Us

If you have any questions or suggestions, please feel free to email us at yukechen_patrick@foxmail.com.



## Authors and Acknowledgements

Authors：

- [Yuke Chen](https://github.com/Patrick-CH) from Wuhan University of Technology
- [Mingxuan Shen](https://github.com/Neige1729) from  Wuhan University of Technology
- [Zizhuo Yu](https://github.com/AdizeroYU) from Wuhan University of Technology



We would like to thank Wuhan University of Technology for providing us with an opportunity to cooperate and collaborate.

We would like to thank Professor Li Lin of WUHAN University of Technology for inspiring our interest in the development of innovative technologies.
