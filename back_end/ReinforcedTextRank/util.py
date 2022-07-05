# -*- encoding:utf-8 -*-
"""
@author:    Patrick
@github:    https://github.com/Patrick-CH
@reference: https://github.com/letiantian/TextRank4ZH
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import math
import re

import networkx as nx
import numpy as np
import sys

HEAD_REINFORCE_RATE = 1.4
TAIL_REINFORCE_RATE = 1.2

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

sentence_delimiters = ['?', '!', ';', '？', '！', '。', '；', '……', '…', '\n']
allow_speech_tags = ['an', 'i', 'j', 'l', 'n', 'nr', 'nrfg', 'ns', 'nt', 'nz', 't', 'v', 'vd', 'vn', 'eng']

PY2 = sys.version_info[0] == 2
if not PY2:
    # Python 3.x and up
    text_type = str
    string_types = (str,)
    xrange = range


    def as_text(v):  ## 生成unicode字符串
        if v is None:
            return None
        elif isinstance(v, bytes):
            return v.decode('utf-8', errors='ignore')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError('Unknown type %r' % type(v))


    def is_text(v):
        return isinstance(v, text_type)

else:
    # Python 2.x
    text_type = unicode
    string_types = (str, unicode)
    xrange = xrange


    def as_text(v):
        if v is None:
            return None
        elif isinstance(v, unicode):
            return v
        elif isinstance(v, str):
            return v.decode('utf-8', errors='ignore')
        else:
            raise ValueError('Invalid type %r' % type(v))


    def is_text(v):
        return isinstance(v, text_type)

__DEBUG = None


def debug(*args):
    global __DEBUG
    if __DEBUG is None:
        try:
            if os.environ['DEBUG'] == '1':
                __DEBUG = True
            else:
                __DEBUG = False
        except:
            __DEBUG = False
    if __DEBUG:
        print(' '.join([str(arg) for arg in args]))


class AttrDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def combine(word_list, window=2):
    """构造在window下的单词组合，用来构造单词之间的边。

    Keyword arguments:
    word_list  --  list of str, 由单词组成的列表。
    windows    --  int, 窗口大小。
    """
    if window < 2: window = 2
    for x in xrange(1, window):
        if x >= len(word_list):
            break
        word_list2 = word_list[x:]
        res = zip(word_list, word_list2)
        for r in res:
            yield r


def get_similarity(word_list1, word_list2):
    """默认的用于计算两个句子相似度的函数。

    Keyword arguments:
    word_list1, word_list2  --  分别代表两个句子，都是由单词组成的列表
    """
    words = list(set(word_list1 + word_list2))
    vector1 = [float(word_list1.count(word)) for word in words]
    vector2 = [float(word_list2.count(word)) for word in words]

    vector3 = [vector1[x] * vector2[x] for x in xrange(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)

    if abs(co_occur_num) <= 1e-12:
        return 0.

    denominator = math.log(float(len(word_list1))) + math.log(float(len(word_list2)))  # 分母

    if abs(denominator) < 1e-12:
        return 0.

    return co_occur_num / denominator


def sort_words(vertex_source, edge_source, window=2, pagerank_config={'alpha': 0.85, }, tf_idf=None,
               head_reinforce=HEAD_REINFORCE_RATE, tail_reinforce=TAIL_REINFORCE_RATE):
    """将单词按关键程度从大到小排序

    Keyword arguments:
    vertex_source   --  二维列表，子列表代表句子，子列表的元素是单词，这些单词用来构造pagerank中的节点
    edge_source     --  二维列表，子列表代表句子，子列表的元素是单词，根据单词位置关系构造pagerank中的边
    window          --  一个句子中相邻的window个单词，两两之间认为有边
    pagerank_config --  pagerank的设置

    tf_idf          --  词频 TF-IDS 的数据(dict)，使得 <tf_idf.keys()> 中的词w权重 *= 1 + 5 * tf_idf[w]
    head_reinforce  --  文章开头20%的增强，使得 <开头的词权重> *= head_reinforce
    tail_reinforce  --  文章结尾20%的增强，使得 <开头的词权重> *= tail_reinforce
    """
    sorted_words = []
    word_index = {}
    index_word = {}
    _vertex_source = vertex_source
    _edge_source = edge_source
    words_number = 0
    for word_list in _vertex_source:
        for word in word_list:
            if not word in word_index:
                word_index[word] = words_number
                index_word[words_number] = word
                words_number += 1

    graph = np.zeros((words_number, words_number))

    for word_list in _edge_source:
        for w1, w2 in combine(word_list, window):
            if w1 in word_index and w2 in word_index:
                index1 = word_index[w1]
                index2 = word_index[w2]
                graph[index1][index2] = 1.0
                graph[index2][index1] = 1.0

    debug('graph:\n', graph)

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)  # this is a dict

    # 依据 TF-IDF 增加权重
    for _idx in range(words_number):
        if index_word[_idx] in tf_idf:
            scores[_idx] *= 1 + 10 * tf_idf[index_word[_idx]]

    # 增加前20%和后20%的权重
    for _idx in range(int(words_number * 0.2)):
        scores[_idx] *= head_reinforce
        scores[words_number - _idx - 1] *= tail_reinforce

    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    for index, score in sorted_scores:
        item = AttrDict(word=index_word[index], weight=score, index=index)
        sorted_words.append(item)

    return sorted_words


def sort_sentences(sentences, words, sim_func=get_similarity, pagerank_config={'alpha': 0.85, },
                   head_reinforce=HEAD_REINFORCE_RATE, tail_reinforce=TAIL_REINFORCE_RATE):
    """将句子按照关键程度从大到小排序

    Keyword arguments:
    sentences         --  列表，元素是句子
    words             --  二维列表，子列表和sentences中的句子对应，子列表由单词组成
    sim_func          --  计算两个句子的相似性，参数是两个由单词组成的列表
    pagerank_config   --  pagerank的设置
    head_reinforce  --  文章开头20%的增强，使得 <开头的句子权重> *= head_reinforce
    tail_reinforce  --  文章结尾20%的增强，使得 <开头的句子权重> *= tail_reinforce
    """
    sorted_sentences = []
    _source = words
    sentences_num = len(_source)
    graph = np.zeros((sentences_num, sentences_num))

    for x in xrange(sentences_num):
        for y in xrange(x, sentences_num):
            similarity = sim_func(_source[x], _source[y])
            graph[x, y] = similarity
            graph[y, x] = similarity

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)  # this is a dict

    #  增加前20%和后20%句子的权重
    for _idx in range(int(sentences_num * 0.2)):
        scores[_idx] *= head_reinforce
        scores[sentences_num - _idx - 1] *= tail_reinforce

    #  优化权重
    for _idx in range(sentences_num):
        #  减少状语权重
        if re.match("(^作为.*)|(.*强调$)|(.*[0-9]+日$)|(.*[0-9]+月$)|(.*[0-9]+年$)|(.*[0-9]+时$)|(.*[0-9]+日电$)|"
                    "(.*指出$)|(在.*时$)|(在.*上$)", sentences[_idx]):
            scores[_idx] = 0
        #  减少长句权重
        if len(sentences[_idx]) > 40:
            scores[_idx] = 0
        elif len(sentences[_idx]) > 30:
            scores[_idx] *= 0.6

    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    for index, score in sorted_scores:
        item = AttrDict(index=index, sentence=sentences[index], weight=score)
        sorted_sentences.append(item)

    return sorted_sentences


if __name__ == '__main__':
    pass
