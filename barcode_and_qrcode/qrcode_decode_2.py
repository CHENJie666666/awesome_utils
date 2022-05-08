"""
二维码解码
"""

import sys
import cv2

def decoder(image):
    img = cv2.imread(image)
    det = cv2.QRCodeDetector()  # 创建二维码识别器
    val, pts, st_code = det.detectAndDecode(img)  # 识别二维码
    
    return val

if __name__ == '__main__':
    pic_path = sys.argv[1]
    data = decoder(pic_path)
    print(data)
