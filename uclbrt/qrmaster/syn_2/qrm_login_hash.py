# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
class HashClass:
    def __init__(self):
        pass
    def md5(str):
        m = hashlib.md5(str.encode("utf-8"))
        return m.hexdigest()

    # 抓取页面的hash值
    def get_hash_value(self, html_doc):
        soup = BeautifulSoup(html_doc, "html.parser")
        # print(soup.prettify())
        info = soup.find_all("div", class_="card")
        for i in info:
            hash = i['data-hash']
        return hash
    # 处理从网页得到的hash值
    def handle_hash(self, data, hash):
        # hash 规则为 MD5（密码+md5(mobile)）+$("#login-container").data("hash"))
        mobile_pwd = HashClass.md5(data['password'] + HashClass.md5(data['mobile']))
        mobile_pwd_hash = mobile_pwd + hash
        data['hash'] = HashClass.md5(mobile_pwd_hash)
        return data

