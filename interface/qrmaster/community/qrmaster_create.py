# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
#md5加密,返回二进制
login_url = 'http://115.29.142.212:8020/Home/Public/login'
link = "http://115.29.142.212:8021/Bpass/Public/login.html"
data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
def login():
    req = requests.session()
    data = req.get(link)
    vcode = input("请输入验证码")
    data['vcode'] = vcode
    r = req.post(login_url,data=data)
    print(r.text)
if __name__ == "__main__":
    #登陆锁掌柜
    login()







