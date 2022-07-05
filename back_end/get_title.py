# -*- encoding:utf-8 -*-
from operator import le
import re
from ReinforcedTextRank.ReTextRankSeq import ReTextRankSeq


def optimize(title):
    '''
    优化标题
    :param title: 标题
    :return: title --优化后的标题
    '''
    #  去掉落单的引号
    if re.match('^”', title) and '“' not in title:
        title = title.replace('”', '')
    if re.match('^“', title) and '”' not in title:
        title = title.replace('“', '')
    #  去掉首尾的引号
    if re.match("^“.*”$", title):
        title = title.replace('”', '')
        title = title.replace('“', '')

    if re.match("强调.*", title):
        title = title.replace('强调', '')
    title = re.sub('(.*强调了)|(.*强调.*：)|(.*强调)|(^是)|(^也是)|(^尤其是)|(^这是)|(^这只是)|(^就是)|(^但是)|(^这就是)|(^背后是)|(^今年是)', '', title)
    return title


def preprocess(content: str) -> str:
    content = content.replace('\n', '。')
    content = content.replace('日电', '日电。')
    content = content.replace('。。', '。')
    content = content.replace('，', '。')
    return content


def get_title(content: str):
    """
    预测文章标题
    :param content: str 文章内容，utf-8编码
    :return:  title: str 预测的标题
    """
    content = preprocess(content)
    rtrs = ReTextRankSeq()
    rtrs.analyze(text=content)
    sentences = rtrs.get_key_sentences()
    if len(sentences) == 0:
        return ''
    title = sentences[0].sentence
    title = optimize(title)

    if len(title) <= 5:
        title += '，' + sentences[1].sentence
        title = optimize(title)

    return title


if __name__ == '__main__':
    pass
