# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
#md5加密,返回二进制
host = 'http://115.29.142.212:8020'
login_url = host +'/Home/Public/login'
link = host+ '/login.html'
data = {
    "mobile": "13326528030",
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
    res = s.post(host+'/Home/Room/addBuilding',data=build_data)
    print(res.text)
def add_floor(s):
    #爬取楼栋号
    floor_url = host + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text)
    with open('./floor_html.txt', 'wb') as fd:
        fd.write(req.content)
    floor_html = soup.find('option')
    build_no = floor_html['value']
    #请求楼层数据
    floor_data = {
        'build':build_no,
        'floors[0][name]':'楼层1',
        'floors[0][num]':'123',
        'floors[0][desc]':'楼层1'
    }
    add_floor_url = host+'/Home/Room/addFloors'
    req = s.post(add_floor_url,data=floor_data)
    print('floor:'+req.text)
def crawler_bulid(s):
    # 爬取楼栋号
    floor_url = host + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text)
    with open('./floor_html.txt', 'wb') as fd:
        fd.write(req.content)
    floor_html = soup.find('option')
    build_no = floor_html['value']
    # 请求楼层数据
    return build_no
#爬取楼层
def crawler_floor(s):
    # 爬取楼层号
    floor_url = host + '/floor.html'
    req = s.get(floor_url)
    soup = BeautifulSoup(req.text)
    floor_html = soup.find('div',id_='doc-center-body')
    #floor_no = floor_html['value']
    print(floor_html)
    #print(floor_no)
    #return floor_no
def add_room(s):
    build_no = crawler_bulid(s)
    floor_no = crawler_floor(s)
    add_room_url = host+'/Home/Room/addRooms'
    room_data = {
        'build':build_no,
        'floor':floor_no,
        'rooms[0][name]':'房间1',
        'rooms[0][num]':'1',
        'rooms[0][no]':'1',
        'rooms[0][locktype]':'1',
        'rooms[0][layout]':'{"translate": {"x": 0,"y": 0},"width": 80,"height": 80}'
    }
    req = s.post(add_room_url,room_data)
    print('room:'+req.text)

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
    #获取最后一个no，发送请求
    group_no = no_list[-1]
    group_data = {
        'no':group_no,
        'return':'/userCenter.html'
    }
    #/Home/CommunityPage/entry.html?no=LbW02pANmE5R68qX&return=/userCenter.html
    req_url = host+'/Home/CommunityPage/entry.html?'+'no='+group_no+'&return=%2FuserCenter.html'
    s.get(req_url,data=group_data)
    req_usecenter_url = host +'/userCenter.html'
    s.get(req_usecenter_url)
    add_room(s)
if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    a  = s.post(login_url, data=data)
    #create_community(s)
    #切换到认证集群
    change_commuity(s)








