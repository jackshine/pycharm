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
    soup = BeautifulSoup(html_doc,"html.parser")
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
        "address":"guangdong",
        "representative":"555",
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
        'file':open(r'./demo.png','rb')}
    response = s.post(up_image_url,files=img_file).json()
    file_url = response['data']['filename']
    return file_url
def change_commuity(s):
    #community_no = get_no(s)
    info = s.get(host+'/userCenter.html')
    with open('./userCenter.txt','wb') as fd:
        fd.write(info.content)
    main_info = BeautifulSoup(info.text,"html.parser")
    com_list = main_info.find('ul',id='communitySwitch')
    #print(com_list.find('ul',class_='dropdown-menu'))
    no_a = com_list.find('ul',class_='dropdown-menu')
    print(type(no_a))
    a_list = no_a.find_all('a')
    print(type(a_list))
    group_no = 0
    for i in a_list:
        if '瑞士-客栈-有为测试' in i.string:
           group_no=i['data-value']
    #获取no，发送请求
    group_data = {
        'no':group_no,
        'return':'/userCenter.html'
    }
    #/Home/CommunityPage/entry.html?no=LbW02pANmE5R68qX&return=/userCenter.html
    req_url = host+'/Home/CommunityPage/entry.html?'+'no='+group_no+'&return=%2FuserCenter.html'
    s.get(req_url,data=group_data)
    req_usecenter_url = host +'/userCenter.html'
    s.get(req_usecenter_url)
    apply_verity(s)
if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a  = s.post(login_url, data=data)
    #create_community(s)
    #切换到认证集群
    change_commuity(s)








