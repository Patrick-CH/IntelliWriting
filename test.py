import json
import time

import pandas as pd
from tqdm import tqdm

from get_abstract import get_abstract
from get_title import get_title


def splits(s: str):
    return [_c for _c in s]


def Rouge_1(result, reference):
    grams_reference = list(splits(reference))
    grams_result = list(splits(result))
    temp = 0
    ngram_all = len(grams_reference)
    for x in grams_reference:
        if x in grams_result:
            temp = temp + 1
    rouge_1 = temp / ngram_all
    return rouge_1


def Rouge_2(result, reference):
    grams_reference = splits(reference)
    grams_model = splits(result)
    gram_2_result = []
    gram_2_reference = []
    temp = 0
    ngram_all = len(grams_reference) - 1
    if ngram_all == 0:
        ngram_all += 1
    for x in range(len(grams_model) - 1):
        gram_2_result.append(grams_model[x] + grams_model[x + 1])
    for x in range(len(grams_reference) - 1):
        gram_2_reference.append(grams_reference[x] + grams_reference[x + 1])
    for x in gram_2_result:
        if x in gram_2_reference:
            temp = temp + 1
    rouge_2 = temp / ngram_all
    return rouge_2


def lcs(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:  # 如果相等，则加入现有的公共子串
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p]


def test(path='data\\dev.json'):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    r1s = []
    r2s = []
    lcs_lens = []
    rls = []
    titles = []
    results = []
    len_res = []

    time_consume = 0.

    for p in tqdm(data):
        title = p['title']
        content = p['content']
        titles.append(title)

        target = title

        tik = time.time()
        pred = get_title(content)
        time_consume += time.time() - tik

        len_res.append(len(pred))
        results.append(pred)

        r1s.append(Rouge_1(pred, target))
        r2s.append(Rouge_2(pred, target))

        if len(pred) != 0:
            lcs_len = len(lcs(pred, target))
            lcs_lens.append(lcs_len)
            precision = lcs_len / len(target)
            recall = lcs_len / len(pred)
            if precision * recall == 0:
                rls.append(0.)
            else:
                rls.append(2 * precision * recall / (precision + recall))
        else:
            rls.append(0.)

    print('Rouge-1', sum(r1s) / len(r1s))
    print('Rouge-2', sum(r2s) / len(r2s))
    print('Rouge-L', sum(rls) / len(rls))
    print('time consume:', time_consume / len(data), ' s')
    print('avg_len', sum(len_res) / len(len_res))

    df = pd.DataFrame()
    df['title'] = titles
    df['pred'] = results
    df['len_pred'] = len_res
    df['rouge_1'] = r1s
    df['rouge_2'] = r2s
    df['rouge_l'] = rls

    path = 'test_result.csv'
    df.to_csv(path)
    print(f'保存至: {path}')

    return sum(r1s) / len(r1s), sum(r2s) / len(r2s), sum(rls) / len(rls)


if __name__ == '__main__':
    test()
