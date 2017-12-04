# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
#md5加密,返回二进制
login_url = 'http://115.29.142.212:8020/Home/Public/login'
link = "http://115.29.142.212:8020/login.html"
data = {
    "mobile": "13480251015",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
def md5(str):
    m = hashlib.md5(str.encode("utf-8"))
    return m.hexdigest()
#抓取页面的hash值
def get_hash(html_doc):
    soup = BeautifulSoup(html_doc)
    # print(soup.prettify())
    info = soup.find_all("div", class_="card")
    for i in info:
        hash = i['data-hash']
    return hash
#处理从网页得到的hash值
def handle_hash(data,hash):
    #hash 规则为 MD5（密码+md5(mobile)）+$("#login-container").data("hash"))
    mobile_pwd = md5(data['password']+md5(data['mobile']))
    mobile_pwd_hash = mobile_pwd+hash
    data['hash'] = md5(mobile_pwd_hash)
if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a = s.post(login_url, data=data)
    print(a.text)






