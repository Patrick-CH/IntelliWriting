[**English**](README.md) | [**中文说明**](README_ZH.md)

# IntelliWriting

IntelliWriting is an intelligent writing tool based on an improved version of TextRank that intelligently generates titles and abstract.



## Introduction

Title prediction has always been an important task in the field of NLP. According to the different characteristics of text, researchers and algorithm engineers have proposed a variety of algorithms to predict the title and abstract. Among them, [TextRank](https://aclanthology.org/W04-3252.pdf) , improved from Google's [PageRank](https://en.wikipedia.org/wiki/PageRank), is an important text summarization algorithm. In this project, TextRank is improved to a certain extent. Not only the summary calculation is realized, but also the title prediction is successfully achieved. The test results in the news data from [Xuexiqiangguo](https://www.xuexi.cn/) reach 19.3% rouge-L effect.

### Abstract

Project Structure

```文件树
├── app.py
├── forms.py
├── get_abstract.py
├── get_title.py
├── ReinforcedTextRank
│   ├── __init__.py
│   ├── ReTextRankKeyword.py
│   ├── ReTextRankSeq.py
│   ├── Segmentation.py
│   ├── stopwords.txt
│   ├── tf-idf.json
│   └── util.py
└── test.py
```



- app.py	Use Flask to provide Internet service
- ReinforcedTextRank   Improved TextRank algorithm package using knowledge enhancement
  - ReTextRankKeyword.py   predict keywords
  - ReTextRankSeq.py   predict sub sequence
  - Segmentation.py   segmentation for passage
  - stopwords.txt   stop words
  - tf-idf.json   TF-IDF data
  - util.py   tools
- get_title.py   predict the title
- get_abstract.py   predict the abstract
- test.py   test the result ( data required )



### Features

We use ReTextRank, an improvement of TextRank, to quickly calculate the headline and summary. On the test set, we could calculate the headline and summary of a news story in an average of 0.1s.



### Test

We use the news data from [Xuexiqinagguo](https://www.xuexi.cn/)：

| Test   | Rouge-1 | Rouge-2 | Rouge-L |
| ------ | ------- | ------- | ------- |
| result | 32.5    |         | 19.3    |



## Install & Use

### Requirements

Our project supports Windows and Linux systems, but you must meet the following requirements:

- python 3.7 +
- Flask
  - flask_wtf
- Numpy
- networkx



### Optional

These two packages are not required if you do not need to run the test program test.py

- Pandas
- tqdm

### Tutorial

You can install our system by following steps：

1.downloads：

```shell
git clone https://github.com/Patrick-CH/IntelliWriting.git
```

2.install required packages

```shell
pip install flask
pip install flask_wtf
pip install numpy
pip install networkx
```

3.run the system：

```shell
cd IntelliWriting
python3 app.py
```

4.use the API
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
