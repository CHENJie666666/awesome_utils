"""
生成二维码
"""

from MyQR import myqr

def qrcode_generator_with_background(data, scale, save_file_path, background):
    """
    生成带有背景图或者动态图的二维码
    params:
        data: 数据
        scale: 大小
        save_file_path: 保存路径
        background: 背景图（支持".jpg"/".png"/".bmp"/".gif"格式）
    """
    myqr.run(
        words=data,
        version=scale,
        picture=background,
        colorized=True,
        save_name=save_file_path,
    )


# 生成带有背景图或者动态图的二维码
data = "I love you, my little baby!"
save_file_path = "./qrcode.png"
scale = 4
background = './background.png'
qrcode_generator_with_background(data, scale, save_file_path, background)

