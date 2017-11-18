# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
#md5加密,返回二进制
login_url = 'http://115.29.142.212:8021/Bpass/Public/doLogin'
link = "http://115.29.142.212:8020/login.html"
data = {
    "mobile": "13480251015",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
commnity_data = {"cname":"有为集群",
        "universalTime":"5",
        "desc":"333",
        "type":"1",
        "addr":"11",
        "cont":"联系人",
        "phone":'13480251015',
        "areaCode":"1"
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
def login():
    req = requests.session()
    html_doc = req.get(link).text
    hash = get_hash(html_doc)
    handle_hash(data, hash)
    req.post(login_url, data=data)
    return req
def create_community(req):
    commnity_create = req.post("http://115.29.142.212:8020/Home/Community/create", commnity_data)
    print(commnity_create.text)
if __name__ == "__main__":
    #登陆锁掌柜
    req = login()
    #创建集群
    # create_community()






