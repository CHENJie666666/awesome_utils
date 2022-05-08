"""
实现中文简体与繁体的相互转化
支持以下文字：
zh-cn 大陆简体
zh-sg 马新简体（马来西亚和新加坡使用的简体汉字）
zh-tw 台灣正體（台湾正体）
zh-hk 香港繁體（香港繁体）
zh-hans 简体
zh-hant 繁體（繁体）
"""

import argparse
import zhconv
import os

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现中文简体与繁体的相互转化")

    parser.add_argument("-s", "--src_file_path", type=str, 
                            help="目标文件所在目录或路径")
    parser.add_argument("-r", "--reversed", default=False, action='store_true',
                            help="指定该参数时表示简体转繁体")

    args = parser.parse_args()
    return args

def simplified_to_traditional(text):
    """
    简体转繁体
    """
    return zhconv.convert(text, 'zh-hant')

def traditional_to_simplified(text):
    """
    简体转繁体
    """
    return zhconv.convert(text, 'zh-cn')


def text_transformation(src_file_path, reversed=False):
    """
    读取文件，实现简体繁体转化后保存为新文件
    """
    # 对单个txt文件进行处理
    if src_file_path.endswith('.txt'):
        
        with open(src_file_path, 'r', encoding='utf-8') as r:
            text = r.read()
            
        if reversed:
            new_text = simplified_to_traditional(text)
            dst_file_path = src_file_path.rsplit('.', 1)[0] + '_hant.txt'
        else:
            new_text = traditional_to_simplified(text)
            dst_file_path = src_file_path.rsplit('.', 1)[0] + '_cn.txt'
        
        with open(dst_file_path, 'w', encoding='utf-8') as w:
            w.write(new_text)
        
        print('{}文件转换完毕'.format(src_file_path))
    
    # 对目录进行处理
    else:
        files = [file for file in os.listdir(src_file_path) if file.endswith('.txt')]
        print('共有{}个文件待转换'.format(len(files)))
        
        for file in files:
            text_transformation(os.path.join(src_file_path, file), reversed)

        print('全部文件转换完毕')

if __name__ == '__main__':
    args = argv_parse()
    text_transformation(args.src_file_path, args.reversed)

