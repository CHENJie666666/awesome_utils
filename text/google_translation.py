"""
调用谷歌翻译实现多语种翻译功能
"""

import argparse
import googletrans
import os
from googletrans import Translator
from language import LANG

# # 输出google支持的语言类型
# print(googletrans.LANGUAGES)

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="谷歌翻译功能")

    parser.add_argument("-t", "--text", type=str, 
                            help="待翻译文本，或待翻译文件所在路径")
    parser.add_argument("-d", "--dest_lang", default='en',
                            help="目标翻译语种")

    args = parser.parse_args()
    return args


def translate(txt_or_file, dest_lang='en'):
    """
    根据输入参数进行判断
    """
    if os.path.isfile(txt_or_file):        
        translate_file(txt_or_file, dest_lang=dest_lang)
    else:
        output = translate_txt(txt_or_file, dest_lang=dest_lang)
        print(f'The translation result ({LANG[dest_lang]}):')
        print(output)


def translate_txt(text, dest_lang='en', src_lang='auto'):
    """
    翻译文本
    输入：
        text  文本内容
        dest_lang  目标语种
        src_lang  输入语种
    输出：
        out.text  翻译文本
    """
    translater = Translator()
    out = translater.translate(text, dest=dest_lang, src=src_lang)
    return out.text


def translate_file(file, dest_lang='en', src_lang='auto'):
    """
    翻译文件中的文本内容
    输入：
        file  文件路径
        dest_lang  目标语种
        src_lang  输入语种
    输出：
        save_file  保存文件路径
    """
    with open(file, 'r', encoding='utf-8') as r:
        text = r.readlines()
    
    translater = Translator()
    out = translater.translate(text, dest=dest_lang, src=src_lang)
    
    # 保存翻译结果
    save_file = os.path.splitext(file)[0] + '_' + dest_lang + os.path.splitext(file)[1]
    with open(save_file, 'w', encoding='utf-8') as w:
        for line in out:
            w.write(line.text)
            w.write('\n')
    
    print('The translated file has been saved as:', save_file)

    return save_file

if __name__ == '__main__':
    args = argv_parse()
    translate(args.text, args.dest_lang)
