# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
import re
#md5加密,返回二进制
host_client = 'http://115.29.142.212:8020'
login_url = host_client +'/Home/Public/login'
link_client = host_client+ '/login.html'
create_url = host_client + '/Home/Community/create'
auth_url = host_client +'/authentication.html'
up_image_url = host_client + '/Home/File/upload'
apply_verify_url = host_client + '/Home/CommunityCenter/postAuthenticationCompany'

#bpass
host_bpass = "http://115.29.142.212:8021"
login_url = host_bpass+'/Bpass/Public/doLogin'
link_bpass = host_bpass+'/Bpass/Public/login.html'
data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
data = {
    "mobile": "13480251015",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
community_data = {
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
#申请审核
def apply_verity(s):
    img_url = up_image(s)
    print(host_client+img_url)
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
#上传图片
def up_image(s):
    img_file = {
        'config':(None,'comVerify'),
        'file':open(r'./demo.png','rb')}
    response = s.post(up_image_url,files=img_file).json()
    file_url = response['data']['filename']
    return file_url
def change_commuity(s):
    info = s.get(host_client+'/userCenter.html')
    with open('./userCenter.txt','wb') as fd:
        fd.write(info.content)
    main_info = BeautifulSoup(info.text,"html.parser")
    com_list = main_info.find('ul',id='communitySwitch')
    no_a = com_list.find('ul',class_='dropdown-menu')
    a_list = no_a.find_all('a')
    group_no = 0
    for i in a_list:
        if community_data['cname'] in i.string:
           group_no=i['data-value']
    #获取no，发送请求
    group_data = {
        'no':group_no,
        'return':'/userCenter.html'
    }
    req_url = host_client+'/Home/CommunityPage/entry.html?'+'no='+group_no+'&return=%2FuserCenter.html'
    s.get(req_url,data=group_data)
    req_usecenter_url = host_client +'/userCenter.html'
    s.get(req_usecenter_url)
    #申请认证
    apply_verity(s)
def login(req):
    html_doc =req.get(link_bpass).text
    soup = BeautifulSoup(html_doc)
    #print(soup.prettify())
    img = soup.find("img",{"id":"imgcode"})
    img_path = host_bpass+img["src"]
    #req.get()得到一个response对象，对象存服务器返回的信息，
    #返回的页面会存在.content和.text对象。
    #.content返回的是字节码
    #.text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
    while True:
        image = req.get(img_path,stream=True).content
        with open('demo.jpg','wb') as fd:
            fd.write(image)
        vcode = input("请输入验证码")
        data['vcode'] = vcode
        r = req.post(login_url, data=data).json()
        print(r)
        if r['status']==200:
            break
def pass_group_verity(req):
    query_verify_url = host_bpass + '/Bpass/ComAuthority/company.html'
    group_data = {
        'type':'',
        'status':'',
        'name':'瑞士-客栈-有为测试',
        'no':''
    }
    query_group = req.get(query_verify_url,params=group_data)
    with open('./query_verify_url.txt', 'wb') as fd:
        fd.write(query_group.content)
    soup = BeautifulSoup(query_group.text)
    s_table = soup.find('table', id='questionTalbe')
    a_list = s_table.find_all('a')
    a_href = a_list[-1]['href']
    reObj1 = re.compile('[0-9]+')
    id = reObj1.findall(a_href)[0]
    page_id = reObj1.findall(a_href)[1]
    print(id,page_id)
    #通过审核
    verify_page_url = host_bpass + '/Bpass/ComAuthority/companyStatus/id/' + id + '/userloginID/' + page_id + '.html'
    verify_data = {
        "id": (None, id),
        "status": (None, "3"),
        "agencyId": (None, "1"),
        "representative": (None, "33323"),
        "hotelSign": (None, "00000"),
        "brandTypeId": (None, "1"),
        "typeSignId": (None, "1"),
        "authorityNote": (None, "22244"),
    }
    v = req.post(verify_page_url, files=verify_data)
    print(v.text)
def pass_verity(req):
    #请求企业认证页面，获取最后一页的链接
    company_verify_url = host_bpass+'/Bpass/ComAuthority/company.html'
    response = req.get(company_verify_url)
    with open('./company_verify_page.txt','wb') as fd:
        fd.write(response.content)
    soup = BeautifulSoup(response.text)
    page_list = soup.find_all('a',class_='num')
    #得到最后一页的链接
    page_list_url = page_list[-1]['href']
    #请求最后一页的链接，获取最后一个集群的链接
    res_last_page = req.get(host_bpass+page_list_url)
    with open('./res_last_page.txt','wb') as fd:
        fd.write(res_last_page.content)
    soup = BeautifulSoup(res_last_page.text)
    last_community_list = soup.find_all('a',class_='btn btn-primary btn-sm')
    last_community = last_community_list[-1]['href']
    print(last_community)
    reObj1 = re.compile('[0-9]+')
    #得到集群的id
    id = reObj1.findall(last_community)[0]
    page_id = reObj1.findall(last_community)[1]

    #拼接审核页面，通过审核
    #http://115.29.142.212:8021/Bpass/ComAuthority/companyStatus/id/581/userloginID/1623.html
    verify_page_url = host_bpass+'/Bpass/ComAuthority/companyStatus/id/'+id+'/userloginID/'+page_id+'.html'
    print(verify_page_url)
    verify_data ={
        "id":(None,id),
        "status":(None,"3"),
        "agencyId":(None,"1"),
        "representative":(None,"33323"),
        "hotelSign":(None,"00000"),
        "brandTypeId":(None,"1"),
        "typeSignId":(None,"1"),
        "authorityNote":(None,"22244"),
    }
    v = req.post(verify_page_url,files=verify_data)
    print(v.text)
if __name__ == "__main__":
    s = requests.session()
    cname = input("输入创建集群的名字：")
    community_data['cname'] = cname
    html_doc = s.get(link_client).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a  = s.post(login_url, data=data)
    create_community(s)
    #切换到认证集群
    change_commuity(s)
    #登录后台，通过审核
    req = requests.session()
    login(req)
    pass_group_verity(req)








