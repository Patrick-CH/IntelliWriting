import argparse
import json
import os

import jieba
import pandas as pd
import torch
from tqdm import tqdm
from transformers import BertTokenizer, GPT2LMHeadModel

from generate_title import predict_one_sample


def Rouge_1(result, reference):
    terms_reference = jieba.cut(reference)
    terms_result = jieba.cut(result)
    grams_reference = list(terms_reference)
    grams_result = list(terms_result)
    temp = 0
    ngram_all = len(grams_reference)
    for x in grams_reference:
        if x in grams_result:
            temp = temp + 1
    rouge_1 = temp / ngram_all
    return rouge_1


def Rouge_2(result, reference):
    terms_reference = jieba.cut(reference)
    terms_result = jieba.cut(result)
    grams_reference = list(terms_reference)
    grams_model = list(terms_result)
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
            if s1[i] == s2[j]: # 如果相等，则加入现有的公共子串
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p]


def test(pred_func, path='data_abs\\dev.json', **kwargs):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    r1s = []
    r2s = []
    lcs_lens = []
    rls = []
    titles = []
    results = []
    len_res = []

    for p in tqdm(data):
        title = p['title']
        content = p['content']
        titles.append(title)

        target = title

        pred = pred_func(content, **kwargs)
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
    print('avg_len', sum(len_res) / len(len_res))

    df = pd.DataFrame()
    df['title'] = titles
    df['pred'] = results
    df['len_pred'] = len_res
    df['rouge_1'] = r1s
    df['rouge_2'] = r2s
    df['rouge_l'] = rls

    path = 'test_result_' + pred_func.__name__ + '.csv'
    df.to_csv(path)
    print(f'保存至: {path}')

    return sum(r1s) / len(r1s), sum(r2s) / len(r2s), sum(rls) / len(rls)


def set_args():
    """设置模型预测所需参数"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='0', type=str, help='设置预测时使用的显卡,使用CPU设置成-1即可')
    parser.add_argument('--model_path', default='trained_model/model1', type=str, help='模型文件路径')
    parser.add_argument('--vocab_path', default='vocab/vocab.txt', type=str, help='词表，该词表为小词表，并增加了一些新的标记')
    parser.add_argument('--batch_size', default=3, type=int, help='生成标题的个数')
    parser.add_argument('--generate_max_len', default=32, type=int, help='生成标题的最大长度')
    parser.add_argument('--repetition_penalty', default=1.2, type=float, help='重复处罚率')
    parser.add_argument('--top_k', default=5, type=float, help='解码时保留概率最高的多少个标记')
    parser.add_argument('--top_p', default=0.95, type=float, help='解码时保留概率累加大于多少的标记')
    parser.add_argument('--max_len', type=int, default=512, help='输入模型的最大长度，要比config中n_ctx小')
    return parser.parse_args()


if __name__ == '__main__':
    """主函数"""
    # 设置预测的配置参数
    args = set_args()
    # 获取设备信息
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICE"] = args.device
    device = torch.device("cuda" if torch.cuda.is_available() and int(args.device) >= 0 else "cpu")
    # 实例化tokenizer和model
    tokenizer = BertTokenizer.from_pretrained(args.vocab_path, do_lower_case=True)
    model = GPT2LMHeadModel.from_pretrained(args.model_path)
    model.to(device)
    model.eval()

    def pred(content):
        titles = predict_one_sample(model, tokenizer, device, args, content)
        return titles[0]

    test(pred)
