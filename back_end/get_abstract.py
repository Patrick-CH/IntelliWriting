# -*- encoding:utf-8 -*-
import json

from tqdm import tqdm

from ReinforcedTextRank.ReTextRankSeq import ReTextRankSeq


def get_abstract(content, num_sentence=6):
    paser = ReTextRankSeq()
    paser.analyze(text=content, lower=True, source='all_filters')
    summary_sentences = paser.get_key_sentences(num=num_sentence, sentence_min_len=6)
    summary_sentences.sort(key=lambda x: x.index, reverse=False)
    summary = '。'.join([_i.sentence for _i in summary_sentences]) + '。'
    return summary


if __name__ == '__main__':
    pass
