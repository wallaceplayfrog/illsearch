from aip import AipOcr
import json

""" 你的 APPID AK SK """
APP_ID = '16101061'
API_KEY = 'vY4bYqPNiuFvBOQU6AbQ0Hl7'
SECRET_KEY = 'wPFx2pX5MtUlZ0WDBo2l43PxAq8r81fU'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
      
for i in range(1, 100):
    image = get_file_content('./已裁剪病历/cutted/bingli ({0}).png'.format(str(i)))
    print(client.basicAccurate(image))
    with open('./已裁剪病历/json/bingli ({}).json'.format(str(i)), 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(client.basicAccurate(image), ensure_ascii = False, indent = 4))