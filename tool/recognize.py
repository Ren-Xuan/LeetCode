import base64
import time
from aip import AipOcr
from pathlib import Path, PurePath
print("aa")
def readFiles(path):
    files = []
    p = Path(path)
    for x in p.iterdir():
        if PurePath(x).match('*.png'):
            files.append(x)
    return files

print('end')
APP_ID = '26113539'
API_KEY = 'XmaBkvDhdX2s493zyErFL5Gy'
SECRET_KEY = '8DTGr0KYmmiVdxFYx2ZiAzNeexhRGHLK'
""" client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
import json
res = []
for file in files:
    with open(file,'rb') as f:
        image = f.read()
    result = client.basicGeneral(image)['words_result']#arr
    text = ""
    for word in result:
        print(word['words'])
        text = text +str(word['words'], "utf-8")
    res.append(text)
for e in res:
    print(e)
for i,word in enumerate(res):
    with open((str(files[i]).split('.')[0])+'.txt','wb') as f:
        f.write(word)
print('endend')
 """
import sys
import json
import base64


# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus


# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'XmaBkvDhdX2s493zyErFL5Gy'

SECRET_KEY = '8DTGr0KYmmiVdxFYx2ZiAzNeexhRGHLK'


OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()


    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

if __name__ == '__main__':

    # 获取access token
    token = fetch_token()
    files = readFiles('D:/aaa/nig')
    for e in files:
        print(e)
    # 拼接通用文字识别高精度url
    image_url = OCR_URL + "?access_token=" + token

    text = ""
    for file in files:
        # 读取测试图片
        file_content = read_file(file)

        # 调用文字识别服务
        result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))

        # 解析返回结果
        result_json = json.loads(result)
        text = ""
        for words_result in result_json["words_result"]:
            for word in words_result['words']:
                text = text + word+"\n"
        time.sleep(3)
        # 打印文字
        print(text)
        with open((str(file).split('.')[0])+'.txt','w') as f:
            f.write(text.replace('\n',""))