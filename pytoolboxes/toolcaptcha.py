# -*- coding: utf-8 -*-
# @Date    : 2021/10/03
# @Author  : 薄荷你玩
# @Website ：http://www.bhshare.cn

import json
import requests

TOKEN = 'free'  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址

def imgcode_online(imgurl):
    """
    在线图片识别
    :param imgurl: 在线图片网址 / 图片base64编码（包含头部信息）
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'online',
        'uri': imgurl
    }
    response = requests.post(URL, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'

def imgcode_local(imgpath):
    """
    本地图片识别
    :param imgpath: 本地图片路径
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'local'
    }

    # binary上传文件
    files = {'file': open(imgpath, 'rb')}

    response = requests.post(URL, files=files, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


if __name__ == '__main__':
    pass
