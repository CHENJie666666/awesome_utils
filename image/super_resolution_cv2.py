import sys
import cv2
from cv2 import dnn_superres

def dnn_super_resolution(src_img_path, model='espcn', multiple=4):
    """
    使用DNN神经网络实现超分
    参数：
        src_img_path：原始图片存储路径
        model：使用的超分模型
            'espcn'：模型小，合成速度快，生成图片小，可以将分辨率提升2/3/4倍
            'edsr'：模型大，合成速度慢，生成图片大，可以将分辨率提升2/3/4倍
            'fsrcnn'：模型小，合成速度快，生成图片大，可以将分辨率提升2/3/4倍
            'lapsrn'：模型适中，合成速度适中，生成图片小，可以将分辨率提升2/4/8倍
        multiple：提升倍数
    """
    print('loading...')
    
    assert model in ['espcn', 'edsr', 'fsrcnn', 'lapsrn'], 'you give the wrong model name!!!'

    if model == 'lapsrn':
        if multiple < 4:
            multiple = 2
        elif multiple < 8:
            multiple = 4
        else:
            multiple = 8
    else:
        if multiple < 3:
            multiple = 2
        elif multiple < 4:
            multiple = 3
        else:
            multiple = 4

    dst_img_path = src_img_path.rsplit('.', 1)[0] + '_' + model + '_' + str(multiple) \
        + '.' + src_img_path.rsplit('.', 1)[1]

    # print(dst_img_path)
    sr = dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(src_img_path)
    path = './super_resolution_cv2_models/' + model.upper() + '_x' + str(multiple) + '.pb'
    sr.readModel(path)

    sr.setModel(model, multiple)
    result = sr.upsample(image)
    cv2.imwrite(dst_img_path, result)
    print('file has been saved as {}'.format(dst_img_path))

if __name__ == '__main__':
    src_img_path = sys.argv[1]
    
    try:
        model = sys.argv[2] 
    except:
        model = 'espcn'
    
    try:
        multiple = int(sys.argv[3]) 
    except:
        multiple = 4
    
    dnn_super_resolution(src_img_path, model=model, multiple=multiple)
