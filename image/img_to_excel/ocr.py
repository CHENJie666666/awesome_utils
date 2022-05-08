from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64

# OCR识别封装
class OCR(object):

    def img_to_excel(self,
                     output_file_name,
                     image_path,
                     secret_id,
                     secret_key):
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential(
            secret_id,
            secret_key
        )
        # 实例化client对象
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        clientProfile.signMethod = "TC3-HMAC-SHA256"
        client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)
        # 实例化一个请求对象
        #req = models.GeneralFastOCRRequest()
        req = models.GeneralFastOCRRequest()
        # 读取图片数据，使用Base64编码
        with open(image_path, 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        req.ImageBase64 = image_base64
        # 通过client对象调用访问接口，传入请求对象
        resp = client.RecognizeTableOCR(req)
        # 获取返回数据（Data为Base64编码后的Excel数据）
        data = resp.Data
        # 转换为Excel
        output_file_name = str(output_file_name)
        path_excel = output_file_name.rsplit('.', 1)[0] + ".xlsx"
        with open(path_excel, 'wb') as f:
            f.write(base64.b64decode(data))
        return path_excel