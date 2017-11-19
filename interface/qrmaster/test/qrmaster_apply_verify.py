# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
#md5加密,返回二进制
host = 'http://115.29.142.212:8020'
login_url = host +'/Home/Public/login'
link = host+ '/login.html'
create_url = host + '/Home/Community/create'
auth_url = host +'/authentication.html'
up_image_url = host + '/Home/File/upload'
apply_verify_url = host + '/Home/CommunityCenter/postAuthenticationCompany'
data = {
    "mobile": "13480251015",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
community_data = {"cname":"测试集群-有为",
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
def create_community(s):
    res = s.post(create_url,data=community_data)
    print(res.text)
#申请审核
def apply_verity(s):
    img_url = up_image(s)
    print(host+img_url)
    apply_data = {
        "isforeign":"0",
        "companyname":"畅联",
        "address":"广州",
        "representative":"333",
        "telephone":"13480251015",
        "fax":"",
        "business":"444",
        "bpath":img_url,
        "areaCode":"86"
    }
    response = s.post(apply_verify_url,data=apply_data).json()
    print(response)
#上传图片
def up_image(s):
    img_file = {
        'config':(None,'comVerify'),
        'file':open(r'D:\linyouwei\python\pycharm\interface\qrmaster\community\demo.jpg','rb')}
    response = s.post(up_image_url,files=img_file).json()
    file_url = response['data']['filename']
    return file_url
def change_commuity(s):
    info = s.get(host+'/userCenter.html')
    with open('./community_html.txt','wb') as fd:
        fd.write(info.content)
    main_info = BeautifulSoup(info.text)
    com_list = main_info.find_all('ul',class_='dropdown-menu')
    print(com_list)
    a_list = com_list[-1].find_all('a')
    no_list = []
    for i in a_list:
        no_list.append(i['data-value'])
    print(no_list)
if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a  = s.post(login_url, data=data)
    #create_community(s)
    #切换到认证集群
    change_commuity(s)








