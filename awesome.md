# Awesome_utils

## 音视频处理

### 1. MP4转MP3

#### moviepy

提取MP4文件的MP3音频

- 安装包

```shell
pip install moviepy
```

- 单个mp4文件转化，调用`mp4_to_mp3.py`文件

```shell
python mp4_to_mp3.py -s './a.mp4' 
```

- 多个mp4文件转化，调用`mp4_to_mp3.py`文件

```shell
python mp4_to_mp3.py -s './mp4_dir' 
```



### 2. 文本转语言

#### pyttsx3

使用windows自带语音包实现文本转语音（tts）功能

- 安装包

```shell
pip install pyttsx3
```

- 安装语音包

设置-时间与语言-语音-管理语言-添加语音

添加语音后，可将INPUT_LANG修改为自己电脑上的语音包

- 文本转语言

```shell
python text_to_speech.py -t '你好' -l 'zh-cn' -v 0.6 -r 150
```

- 文件转语音文件

```shell
python text_to_speech.py -t './a.txt' -l 'zh-cn' -s 'a.mp3'
```



## 图像处理

### 1. 图像超分

#### opencv超分

- 安装包

```shell
pip uninstall opencv-python
pip install opencv-contrib-python
```

- 下载模型文件（[opencv_contrib/modules/dnn_superres at master · opencv/opencv_contrib (github.com)](https://github.com/opencv/opencv_contrib/tree/master/modules/dnn_superres)），并存放至代码所在同级目录的super_resolution_cv2_models文件夹中
- 调用`super_resolution_cv2.py`文件

第一个参数为图片文件所在路径

第二个参数为模型类型，可选项为'espcn', 'edsr', 'fsrcnn', 'lapsrn'（默认为'espcn'）

第三个参数为放大倍数，前三个模型可放大2/3/4倍，最后一个模型可以放大2/4/8倍（默认为4）

```shell
python super_resolution_cv2.py './test.png' 'espcn' 4
```



### 2. 图像背景透明处理

#### pillow

- 调用`background_transparent.py`文件

```shell
python background_transparent.py 'test.jpg'
```

- 指定背景色（十六进制或RGB值）

```shell
python background_transparent.py 'test.jpg' -hex '123456'
python background_transparent.py 'test.jpg' -rgb 230 230 230
```



### 2. 图片转excel

#### 腾讯云服务

- 开通腾讯云服务

1. 注册腾讯云账号（可直接用微信注册），并进行实名认证（可获得每月1000次API调用机会）

[云产品免费试用_云服务免费体验_免费云产品试用 - 腾讯云 (tencent.com)](https://cloud.tencent.com/act/free)

2. 开通相关服务
3. 访问管理-访问密钥-新建密钥

- 安装依赖

安装腾讯云python开发工具及pyyaml工具

```shell
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
pip install pyyaml
```

- 调用imgToExcel.py文件

```shell
python imgToExcel.py './1.jpg'
```



## 条形码&二维码

### 1. 二维码生成

#### pyqrcode

不支持中文内容，可生成".svg"/".eps"/".png"格式的静态或者网页二维码文件

- 官方文档

https://pythonhosted.org/PyQRCode/

- 安装包

```shell
pip install pyqrcode -i https://mirror.baidu.com/pypi/simple/
pip install webcolors
```

- 使用

py文件参数修改

```python
data = "I love you, my little baby!" # 网址或文本
save_file_path = "./qrcode.png"  # 生成二维码文件存储路径
background = 'white'  # 二维码背景色
color = 'black'  # 二维码颜色
scale = 4  # 二维码大小
```

运行py文件

```shell
python qrcode_generator_1.py
```

#### MyQr

不支持中文内容，可生成".png"/".gif"格式、带有背景的静态/动态二维码

- 安装包

```shell
pip install myqr
```

- 使用

py文件参数修改

```python
data = "Hello" # 网址或文本
save_file_path = "./qrcode.png"  # 生成二维码文件存储路径
scale = 4  # 二维码大小
background = './background.png'  # 背景图片
```

运行py文件

```shell
python qrcode_generator_2.py
```

#### qrcode

支持中文内容，可生成".png"格式、带有logo的静态二维码

- 安装包

```shell
pip install qrcode
```

- 使用

py文件参数修改

```python
data = "Hello" # 网址或文本
save_file_path = "./qrcode.png"  # 生成二维码文件存储路径
border = 4  # 边框大小
scale = 4  # 二维码大小
box_size = 10  # 每个格子大小
bc = "white"  # 二维码背景色
color = "black"  # 二维码颜色
logo = './1.jpg'  # logo图片的存储路径
```

运行py文件

```shell
python qrcode_generator_3.py
```



### 2. 二维码识别

#### pyzbar

支持含有中英文内容的二维码解码（部分中文可能存在解码乱码现象）

- 安装包

```shell
pip install pyzbar
```

- 使用

运行py文件

```shell
python qrcode_decode_1.py './qrcode2.png'
```

#### opencv

支持含有英文内容的二维码解码（不支持中文）

- 安装包

```shell
pip install opencv-python
```

- 调用`qrcode_decode_2.py`文件

```shell
python qrcode_decode_2.py './qrcode.png'
```





## 文本处理

### 1. 繁体简体互转

实现单一txt文件或目录下所有txt文件的繁体简体互转

- 安装包

```shell
pip install zhconv
```

- 繁体转简体：调用`simp_and_trad_zh_trans.py`文件

```shell
python simp_and_trad_zh_trans.py './a.txt'
```

- 简体转繁体：调用`simp_and_trad_zh_trans.py`文件

```shell
python simp_and_trad_zh_trans.py './a.txt' -r
```

- 多txt同时转换：调用`simp_and_trad_zh_trans.py`文件

```
python simp_and_trad_zh_trans.py './txt_dir'
```



### 2. 谷歌翻译

使用谷歌翻译API实现多语种翻译功能

- 官方文档

https://py-googletrans.readthedocs.io/en/latest/

- 安装包

```shell
pip install googletrans==3.1.0a0 -i https://mirror.baidu.com/pypi/simple/
```

- 直接翻译文本（默认语种为英语）

```shell
python google_translation.py -t '你好' -d 'fr'
```

- 翻译txt文件

```shell
python simp_and_trad_zh_trans.py -t './a.txt'
```



### 3. 语种检测

使用谷歌翻译API实现语种检测功能

- 安装包

```shell
pip install googletrans==3.1.0a0 -i https://mirror.baidu.com/pypi/simple/
```

- 检测文本，输出为语种及置信度

```shell
python language_detection.py -t '你好'
```

