"""
功能：提取MP4文件的MP3音频
"""

from moviepy.editor import VideoFileClip
import os
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现mp4文件向mp3文件的转换")

    parser.add_argument("-s", "--src_file_path", type=str, 
                            help="目标文件所在目录或路径")

    args = parser.parse_args()
    return args

def single_mp4_to_mp3(mp4_path):
    """
    将单个mp4文件转换为mp3文件
    params: 
        mp4_path：mp4文件所在路径
    """
    video = VideoFileClip(mp4_path)
    audio = video.audio
    mp3_path = mp4_path.rsplit('.', 1)[0] + '.mp3'
    audio.write_audiofile(mp3_path)    
    print('mp4文件转换完毕')

def multiple_mp4_to_mp3(mp4_dir):
    """
    将多个mp4文件转换为mp3文件
    params: 
        mp4_dir：mp4文件所在目录
    """
    mp4_names = os.listdir(mp4_dir)
    mp4_files = [name for name in mp4_names if name.endswith('.mp4')]
    print('共有{}个mp4文件待转换'.format(len(mp4_files)))
    
    for i, mp4_file in enumerate(mp4_files):
        mp4_path = os.path.join(mp4_dir, mp4_file)
        
        mp3_file = mp4_file.rsplit('.')[0] + '.mp3'
        mp3_path = os.path.join(mp4_dir, mp3_file)

        video = VideoFileClip(mp4_path)
        audio = video.audio
        audio.write_audiofile(mp3_path)
        
        print('第{}个mp4文件转换完毕'.format(i + 1))

def mp4_to_mp3(file_path):
    # 单个文件处理
    if file_path.endswith('.mp4'):
        single_mp4_to_mp3(file_path)
    # 批量处理
    else:
        multiple_mp4_to_mp3(file_path)

if __name__ == '__main__':
    args = argv_parse()
    mp4_to_mp3(args.src_file_path)

