"""
生成二维码
"""

import qrcode
from PIL import Image


def qrcode_generator(data, save_file_path, border=4, scale=20, box_size=10, 
        bc="white", color="black", logo=None):
    """
    生成二维码（支持中英文），可添加logo
    params:
        data: 数据
        save_file_path: 保存文件路径（可以".svg"/".eps"/".png"结尾，若不给则默认输出至控制台）
        border: 外边框大小
        scale: 二维码大小（1-40，1个单位为12像素）
        box_size: 每个格子像素大小
        bc: 二维码背景色（格式可以为RGB/十六进制/颜色名称）
        color: 二维码颜色
        logo: 二维码中间的logo图像路径
    """
    qr = qrcode.QRCode(
        version=scale,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data=data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=color, back_color=bc)

    # 添加logo
    if logo:
        icon = Image.open(logo)
        
        img_w, img_h = image.size
        factor = 6
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        image.paste(icon, (w, h), mask=None)

    image.save(save_file_path)


# 生成中文的二维码
data = "我是陈杰，".encode('utf-8')
save_file_path = "./qrcode2.png"
border = 4
scale = 20
box_size = 10
bc = "white"
color = "black"
logo = './1.jpg'
qrcode_generator(data, save_file_path, border=border, scale=scale, box_size=box_size, 
        bc=bc, color=color, logo=logo)