# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
#md5加密,返回二进制
host_client = 'http://115.29.142.212:8020'
login_client_url = host_client +'/Home/Public/login'
link_client = host_client+ '/login.html'
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
    soup = BeautifulSoup(html_doc, "html.parser")
    # print(soup.prettify())
    info = soup.find_all("div", class_="card")
    for i in info:
        hash = i['data-hash']
    return hash
#处理从网页得到的hash值


def handle_hash(data ,hash):
    #hash 规则为 MD5（密码+md5(mobile)）+$("#login-container").data("hash"))
    mobile_pwd = md5(data['password']+md5(data['mobile']))
    mobile_pwd_hash = mobile_pwd+hash
    data['hash'] = md5(mobile_pwd_hash)


def add_bulid(s):
    #http://115.29.142.212:8020/Home/Room/addBuilding
    build_data={
        'name':'楼栋1',
        'num':'111',
        'desc':'描述',
        'contact':'负责人',
        'phone':'13480251015',
        'areaCode':'86',
    }
    res = s.post(host_client+'/Home/Room/addBuilding',data=build_data)
    print(res.text)


def add_floor(s):
    #爬取楼栋号
    floor_url = host_client + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text, "html.parser")
    with open('./floor_html.txt', 'wb') as fd:
        fd.write(req.content)
    floor_html = soup.find('option')
    build_no = floor_html['value']
    # 请求楼层数据
    floor_data = {
        'build':build_no,
        'floors[0][name]': '楼层1',
        'floors[0][num]': '121',
        'floors[0][desc]': '楼层1',
    }
    add_floor_url = host_client+'/Home/Room/addFloors'
    req = s.post(add_floor_url,data=floor_data)
    # print('floor:'+req.text)
def crawler_bulid(s):
    # 爬取楼栋号
    floor_url = host_client + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text, "html.parser")
    with open('./floor_html.txt', 'wb') as fd:
        fd.write(req.content)
    floor_html = soup.find('select', id='buildId')
    build_no = floor_html.find('option')['value']
    return build_no


def crawler_floor(s):
    # 爬取楼层号
    floor_url = host_client + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text, "html.parser")
    floor_html = soup.find('div', id='doc-center-body')
    tr_html = floor_html.find_all('tr')
    # print(tr_html)
    td_html = tr_html[-1].find('td',class_='col-xs-3')
    return td_html['data-value']


def add_room(s):
    build_no = crawler_bulid(s)
    floor_no = crawler_floor(s)
    add_room_url = host_client+'/Home/Room/addRooms'
    room_data = {
        'build': build_no,
        'floor': floor_no,
        'rooms[0][name]': '房间1',
        'rooms[0][num]': '1',
        'rooms[0][no]': '1',
        'rooms[0][locktype]': '1',
        'rooms[0][layout]': '{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
    }
    req = s.post(add_room_url, room_data)
    print('room:'+req.text)


def change_commuity(s):
    info = s.get(host_client + '/userCenter.html')
    with open('./userCenter.txt', 'wb') as fb:
        fb.write(info.content)
    main_info = BeautifulSoup(info.text, "html.parser")
    com_list = main_info.find('ul', id='communitySwitch')
    no_a = com_list.find('ul', class_='dropdown-menu')
    a_list = no_a.find_all('a')
    group_no = 0
    for i in a_list:
        if community_data['cname'] in i.string:
            group_no = i['data-value']
    # 获取no，发送请求
    group_data = {
        'no': group_no,
        'return': '/userCenter.html'
    }
    print(group_data)
    req_url = host_client + '/Home/CommunityPage/entry.html'
    s.get(req_url, params=group_data)
    req_usecenter_url = host_client + '/userCenter.html'
    s.get(req_usecenter_url)
    add_room(s)
if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link_client).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a = s.post(login_client_url, data=data)
    cname = input("输入集群")
    community_data['cname'] = cname
    # 切换到认证集群
    change_commuity(s)








