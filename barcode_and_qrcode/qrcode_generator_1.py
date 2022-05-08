"""
生成二维码
"""

from turtle import back
import pyqrcode
import webcolors

def color_to_rgb(color):
    """将颜色从string格式转化为RGB格式"""
    if color.startswith('#'):
        return webcolors.hex_to_rgb(color)
    else:
        return webcolors.name_to_rgb(color) 


def qrcode_generator(data, save_file_path=None, scale=4, bc="white", color="black"):
    """
    生成二维码
    params:
        data: 数据
        save_file_path: 保存文件路径（可以".svg"/".eps"/".png"结尾，若不给则默认输出至控制台）
        scale: 二维码大小
        bc: 二维码背景色（格式可以为RGB/十六进制/颜色名称）
        color: 二维码颜色
    """
    qrc = pyqrcode.create(data)

    # 生成二维码
    if save_file_path:
        # svg格式
        if save_file_path.endswith('.svg'):        
            if isinstance(bc, tuple):
                bc = webcolors.rgb_to_hex(bc)
            if isinstance(color, tuple):
                color = webcolors.rgb_to_hex(color)
            qrc.svg(save_file_path, scale=scale, background=bc, module_color=color)
        # EPS格式
        elif save_file_path.endswith('.eps'):  
            qrc.eps(save_file_path, scale=2)

        # png格式
        elif save_file_path.endswith('.png'):
            if not isinstance(bc, tuple):
                bc = color_to_rgb(bc)    
            if not isinstance(color, tuple):
                color = color_to_rgb(color)  
            qrc.png(save_file_path, scale=scale, background=bc, module_color=color)
    
    # terminal输出
    else:
        # print(qrc.terminal(quiet_zone=1))
        print(qrc.terminal(module_color='red', background='yellow'))



# 生成普通二维码
data = "I love you, my little baby!"
save_file_path = "./qrcode.png"
background = 'white'
color = 'black'
scale = 4 
qrcode_generator(data, save_file_path, scale=scale, bc=background, color=color)

