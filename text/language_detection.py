"""
调用谷歌翻译实现语种类别检测功能
"""

import argparse
import googletrans
from googletrans import Translator
from language import LANG

# # 输出google支持的语言类型
# print(googletrans.LANGUAGES)

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="语种检测功能")

    parser.add_argument("-t", "--text", type=str, 
                            help="待检测文本")

    args = parser.parse_args()
    return args

def detection(text):
    """
    检测文本
    输入：
        text  文本内容
    输出：
        out  检测结果
    """
    if text:
        translater = Translator()
        out = translater.detect(text)

        print(f'Language: {LANG[out.lang.lower()]}')
        print(f'Confidence: {out.confidence}')

    else:
        print('No text!')
        out = None
    
    return out

if __name__ == '__main__':
    args = argv_parse()
    detection(args.text)
