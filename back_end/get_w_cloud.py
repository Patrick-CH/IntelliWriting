import jieba
import wordcloud
import uuid
from PIL import Image
import numpy as np


def generate_wcloud(text: str):    
    mask = np.array(Image.open("mask.jpg"))
    words = jieba.lcut(text)
    words = [_w if len(_w) > 2 else '' for _w in words]
    w = wordcloud.WordCloud(font_path="simsun.ttf", background_color="white", 
        width=800, height=800, colormap='gist_heat', mask=mask)
    w.generate(" ".join(words))
    file_name = f"wordcloud{str(uuid.uuid4())}.png"

    w.to_file(f"wcloud_pics/{file_name}")
    img = Image.open(f"wcloud_pics/{file_name}")
    new_img = Image.blend(img, Image.open("mask.jpg"), 0.5)
    new_img.save(f"wcloud_pics/{file_name}")
    return file_name


if __name__ == '__main__':
    print(generate_wcloud("""
    程序是为进行某项活动所规定的先后次序，体现为一定的规矩。俗话说：“不以规矩，不成方圆。"领导干部自觉增强程序意识，按照程序办事，才能不断推动各项工作落细落小落实。\n习近平同志告诫全党，必须遵循组织程序，重大问题该请示的请示，该汇报的汇报，不允许超越权限办事。对于强化程序意识的重要性，大部分领导干部都比较清楚，但仍有人不愿按程序办事，总爱绕过程序拍肩膀定调、拍脑袋决策、拍胸脯许诺，一旦遇到矛盾就拿权力压人。究其主要原因：一是迷信人情关系。觉得大家平时都很熟悉，没必要走程序，遇事习惯于打招呼。二是浮躁心理影响。平时静不下来学习有关制度和程序，遇事坐不下来分析事情始末缘由，处理问题时总是怕麻烦、图省事，视程序而不见、置程序于不顾。三是私心杂念作怪。
    """))