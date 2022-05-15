"""
文本转语音功能
"""

import os
import pyttsx3
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="文本转语音功能")

    parser.add_argument("-t", "--text", type=str, 
                            help="待检测文本或文件所在路径")
    parser.add_argument("-l", "--lang", type=str, default='zh-cn',
                            help="语种类型，可通过-dis或--display_lang查看支持的语种类型")
    parser.add_argument("-r", "--rate", type=int, default=200, 
                            help="语音播放速率")
    parser.add_argument("-v", "--volumn", type=float, default=1.0, 
                            help="语音播放音量（0~1之间）")
    parser.add_argument("-s", "--save_file", type=str, default=None,
                            help="语音存储路径")
    parser.add_argument("-dis", "--display_lang", default=False, action='store_true',
                            help="查看支持的语种类型")

    args = parser.parse_args()
    return args

INPUT_LANG = {    
    'zh-cn': 
        {
            'voice_id': 0,
            'name': 'Microsoft Huihui Chinese (Simplified)'
        },
    'en-am':
        { 
            'voice_id': 1,
            'name': 'Microsoft David Desktop - English (United States)',
        },
    # 'en-am2':
    #     {
    #     'voice_id': 2,
    #     'name': 'Microsoft Zira Desktop - English (United States)',
    #     },
    'fr': 
        {
            'voice_id': 3,
            'name': 'Microsoft Hortense Desktop - French'
        },
    'ja': 
        {
            'voice_id': 4,
            'name': 'Microsoft Haruka Desktop - Japanese'
        },
    'ko': 
        {
            'voice_id': 5,
            'name': 'Microsoft Heami Desktop - Korean'
        },    
    'en-uk': 
        {
            'voice_id': 6,
            'name': 'Microsoft Hazel Desktop - English (Great Britain)'
        },
    'zh-hk': 
        {
            'voice_id': 7,
            'name': 'Microsoft Tracy Desktop - Chinese(Traditional, HongKong SAR)'
        },
    'zh-tw': 
        {
            'voice_id': 8,
            'name': 'Microsoft Hanhan Desktop - Chinese (Taiwan)'
        },
}

def print_lang_info():
    """
    获取语种类型对应的ID号
    """
    print(f'lang    id  name')
    for key, value in INPUT_LANG.items():
        id = value['voice_id']
        name = value['name']        
        print(f'{key.ljust(5)}   {id}   {name}')


def text_to_speech(text, lang, save_file=None, rate=200, volumn=1.0):
    """
    文本转语音
    参数：
        text  文本内容
        lang  语种类型
        save_file  语音保存路径
        rate  语音播放速度
        volumn  语音播放音量
    """
    # 模块初始化
    engine = pyttsx3.init()
    print('开始文本转语音')

    voices = engine.getProperty('voices')
    voice_id = INPUT_LANG[lang]['voice_id']
    # print(voice_id)
    engine.setProperty('voice', voices[voice_id].id)

    # 调整速率
    # rate = engine.getProperty('rate') # 查看速率
    engine.setProperty('rate', rate)

    # 调整音量
    # volume = engine.getProperty('volume') # 查看音量
    engine.setProperty('volume', volumn)

    if save_file:
        engine.save_to_file(text, save_file)
        print(f'The mp3 file has been saved as {save_file}')
    else:
        engine.say(text)
    
    # 等待语音播报完毕
    engine.runAndWait()


if __name__ == '__main__':
    args = argv_parse()
    
    if args.display_lang:
        print_lang_info()
    
    if args.text:
        if os.path.isfile(args.text):
            with open(args.text, 'r', encoding='utf-8') as r:
                text = r.read()
            text_to_speech(text, args.lang, args.save_file, args.rate, args.volumn)
        else:
            text_to_speech(args.text, args.lang, args.save_file, args.rate, args.volumn)
