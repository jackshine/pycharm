# encoding=utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#md5加密,返回二进制
login_url = 'http://115.29.142.212:8021/Bpass/Public/doLogin'
link = "http://115.29.142.212:8021/Bpass/Public/login.html"
host = "http://115.29.142.212:8021"
data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
def get_code():
    req = requests.session()
    html_doc =req.get(link).text
    soup = BeautifulSoup(html_doc)
    #print(soup.prettify())
    img = soup.find("img",{"id":"imgcode"})
    img_path = host+img["src"]
    #req.get()得到一个response对象，对象存服务器返回的信息，
    #返回的页面会存在.content和.text对象。
    #.content返回的是字节码
    #.text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
    image = req.get(img_path,stream=True).content
    with open('demo.jpg','wb') as fd:
        fd.write(image)
    vcode = input("请输入验证码")
    data['vcode'] = vcode
    r = req.post(login_url, data=data)
    print(r.text)
if __name__ == "__main__":
    get_code()







