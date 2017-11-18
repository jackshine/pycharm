# encoding=utf-8
import requests
import time

login_url = 'http://115.29.142.212:8020/Home/Public/login'
link = "http://115.29.142.212:8010/login.html"
s = requests.session()
b = s.get(link)
print(requests.utils.dict_from_cookiejar(b.cookies))  # cookiesjar转成字典输出
data = {
    "mobile": "13480251015",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d",
}
time.sleep(1)
a = s.post(login_url, data=data)
print(a.text)
