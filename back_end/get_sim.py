import os


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


def get_sim_title(target):
    d = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(d, "titles.txt")) as f:
        exist_titles = f.read().split('\n')
    ls = []
    for i in exist_titles:
        ls.append((i, Rouge_1(target, i)))
    ls.sort(key=lambda x: x[1], reverse=True)
    ls = ls[:3]
    ret = []
    for t, s in ls:
        ret.append({"title": t, "score": s})
    return ret