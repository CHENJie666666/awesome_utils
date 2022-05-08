import sys
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance


def decoder(image):
    img = Image.open(image)
    # img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    # img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    # img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    img = img.convert('L')#灰度化
    img = img.convert("1")

    barcodes = pyzbar.decode(img)
    # print(barcodes)
    data = []
    for barcode in barcodes:
        barcodeData = barcode.data.decode('utf-8')
        data.append(barcodeData)
        # barcodeType = barcode.type
 
        # # 绘出图像上条形码的数据和条形码类型
        # text = "{} ({})".format(barcodeData, barcodeType)
        # print(text)
    if len(data) == 0:
        return None
    elif len(data) == 1:
        return data[0]
    else:
        return data

if __name__ == '__main__':
    pic_path = sys.argv[1]
    data = decoder(pic_path)
    print(data)
