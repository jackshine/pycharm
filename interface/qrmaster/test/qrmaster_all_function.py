# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
import re
#md5加密,返回二进制
host_client = 'http://115.29.142.212:8020'
login_client_url = host_client +'/Home/Public/login'
link_client = host_client+ '/login.html'
create_url = host_client + '/Home/Community/create'
auth_url = host_client +'/authentication.html'
up_image_url = host_client + '/Home/File/upload'
apply_verify_url = host_client + '/Home/CommunityCenter/postAuthenticationCompany'

#bpass
host_bpass = "http://115.29.142.212:8021"
login_bpass_url = host_bpass+'/Bpass/Public/doLogin'
link_bpass = host_bpass+'/Bpass/Public/login.html'
bpass_data = {
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
    rep = s.post(create_url,data=community_data)
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
        'file':open(r'./verify.png','rb')}
    response = s.post(up_image_url,files=img_file).json()
    file_url = response['data']['filename']
    return file_url


def change_commuity(s):
    info = s.get(host_client+'/userCenter.html')
    with open('./userCenter.txt', 'wb') as fb:
        fb.write(info.content)
    main_info = BeautifulSoup(info.text, "html.parser")
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
    print(group_data)
    req_url = host_client+'/Home/CommunityPage/entry.html'
    s.get(req_url,params=group_data)
    req_usecenter_url = host_client +'/userCenter.html'
    s.get(req_usecenter_url)
    return s


def detele_all_room(s):
    # 爬取所有的room_id
    room_info = get_all_room_info(s)
    # 请求删除房间接口
    detele_room_url = host_client + '/Home/Room/deleteRoom'
    for i in room_info:
        data = {
             'room':i['room']
        }
        s.post(detele_room_url, data=data)


def update_room_type(s):
    req_url = host_client + '/Home/Room/saveRoom'
    room_data = get_all_room_info(s)
    for i in room_data:
        print(i)
    for i in range(room_data.__len__()):
        for single_room in room_data:
            single_room['locktype']='1'
            s.post(req_url,data=single_room)

def get_all_room_info(s):
    # 得到每个房间页面的请求链接
    req_index_url = host_client + '/room.html'
    room_html = s.get(req_index_url)
    soup = BeautifulSoup(room_html.text, "html.parser")
    div_tag = soup.find('div', id='doc-center-page')
    # print(table.tbody.tr.next_sibling.next_sibling)
    page_url = div_tag.find_all('a')
    page_url = page_url[:-page_url.__len__():-1]
    page_url_list = []
    for  i in page_url:
        page_url_list.append(i['href'])
    page_url_list.append('room_1.html')
    list_data = []
    for url in page_url_list:
        # 房间id:'room' 房间名：'name'房间号:'no' 锁编号：'num' 锁类型'locktype'
        req_url = host_client + '/'+ url
        data = s.get(req_url)
        soup = BeautifulSoup(data.text, "html.parser")
        table_soup = soup.find('table', id='roomTable')
        # 玫瑰花客栈-测试
        tr_list = table_soup.tbody.find_all('tr')
        #计算tr的数量，得到有多少个房间
        num = 0
        for i in tr_list:
            num += 1
        tr_soup = table_soup.tbody.tr
        td_soup = tr_soup.td
        count = 0
        while True:
            data = {}
            for i in range(16):
                td_soup = td_soup.next_sibling
            data_room = {}
            data_room['room']=td_soup['data-value']
            data_room['name']=td_soup['data-name']
            data_room['no']=td_soup['data-no']
            data_room['num']=td_soup['data-num']
            data_room['locktype']=td_soup['data-locktype']
            list_data.append(data_room)
            count += 1
            if count == num:
                break
            tr_soup = tr_soup.next_sibling
            td_soup = tr_soup.td
    return list_data


def login_bpass(req):
    html_doc =req.get(link_bpass).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    img = soup.find("img",{"id":"imgcode"})
    img_path = host_bpass+img["src"]
    # req.get()得到一个response对象，对象存服务器返回的信息，
    # 返回的页面会存在.content和.text对象。
    # .content返回的是字节码
    # .text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
    while True:
        image = req.get(img_path,stream=True).content
        with open('demo.jpg','wb') as fd:
            fd.write(image)
        vcode = input("请输入验证码")
        bpass_data['vcode'] = vcode
        r = req.post(login_bpass_url, data=bpass_data).json()
        print(r)
        if r['status']==200:
            break


def pass_group_verity(req,community_data):
    query_verify_url = host_bpass + '/Bpass/ComAuthority/company.html'
    group_data = {
        'type': '',
        'status': '',
        'name':community_data['cname'],
        'no': ''
    }
    print(group_data)
    query_group = req.get(query_verify_url,params=group_data)
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
if __name__ == "__main__":
    s = requests.session()
    cname = input("输入集群的名字：")
    # 春日客栈-测试 玫瑰花客栈-测试
    community_data['cname'] = cname
    html_doc = s.get(link_client).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    s.post(login_client_url, data=data)
    # # 创建集群
    # create_community(s)
    # 切换到认证集群
    s = change_commuity(s)
    #申请认证
    # apply_verity(s)
    # 删除所有房间
    detele_all_room(s)
    # update_room_type(s)
    # 登录后台，通过审核
    # req = requests.session()
    # login_bpass(req)
    # pass_group_verity(req,community_data)








