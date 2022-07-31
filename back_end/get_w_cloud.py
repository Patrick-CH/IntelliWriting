import jieba
import wordcloud
import uuid


def generate_wcloud(text: str):
    words = jieba.lcut(text)
    words = [_w if len(_w) > 2 else '' for _w in words]
    w = wordcloud.WordCloud(font_path="simsun.ttf", background_color="white", width=600, height=300, colormap='gist_heat')
    w.generate(" ".join(words))
    file_name = f"wordcloud{str(uuid.uuid4())}.png"
    w.to_file(f"wcloud_pics/{file_name}")
    return file_name


if __name__ == '__main__':
    pass