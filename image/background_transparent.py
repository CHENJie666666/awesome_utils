"""
功能：消除图像背景
"""

from PIL import Image
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现中文简体与繁体的相互转化")

    parser.add_argument("-s", "--src_file_path", type=str, 
                            help="目标文件所在目录或路径")
    parser.add_argument("-m", "--margin", type=int, default=30, 
                            help="容许像素偏差")
    parser.add_argument("-rgb", "--rgb_value", default=None, nargs=3, type=int,
                            help="指定背景色的RGB值")
    parser.add_argument("-hex", "--hex", default=None, nargs=1, type=str,
                            help="指定背景色的十六进制值")

    args = parser.parse_args()
    return args

def hex_to_rgb(hex):
    """
    十六进制转RGB
    """
    if hex[0] != '#' or len(hex) != 7:   
        print('注意：十六进制格式颜色错误，请输入7位以\'#\'开头的字符串\n')
        return None
    else:
        r = int('0x' + hex[1:3], 16)
        g = int('0x' + hex[3:5], 16)
        b = int('0x' + hex[5:7], 16)
        return (r, g, b)

def jpg_to_png(src_img_path, margin=30, bc_color=None):
    """
    将图片的背景变成透明色(jpg-RGB, png-RGBA)
    参数：
        src_img_path：原始图片存储路径
        margin：和背景颜色的差异值
        bc_color：背景颜色值（十六进制或RGB值）
    """
    img = Image.open(src_img_path)
    width, height = img.size
    
    # 获取背景颜色的RGB值
    if bc_color:
        r, g, b = hex_to_rgb(bc_color)
    else:
        pix = img.load()
        if src_img_path.endswith('.jpg'):
            r, g, b = pix[int(width / 20), int(height / 20)]
        elif src_img_path.endswith('.png'):
            r, g, b, a = pix[int(width / 20), int(height / 20)]

    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()

    # 背景填充零透明度
    for item in datas:
        if (item[0] >= max(r - margin, 0) and item[0] <= min(r + margin, 255)) \
            and (item[1] >= max(g - margin, 0) and item[1] <= min(g + margin, 255)) \
            and (item[2] >= max(b - margin, 0) and item[2] <= min(b + margin, 255)):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)

    if src_img_path.endswith('.jpg'):
        save_img_path = src_img_path.rsplit('.', 1)[0] + '.png'
    
    elif src_img_path.endswith('.png'):
        save_img_path = src_img_path.rsplit('.', 1)[0] + '_new.png'
    
    img.save(save_img_path, "PNG")

if __name__ == '__main__':
    args = argv_parse()
    
    if args.rgb_value:
        bc_color = args.rgb_value
    elif args.hex_value:
        bc_color = args.hex_value
    else:
        bc_color = None
        
    jpg_to_png(args.src_img_path, args.margin, bc_color=bc_color)
