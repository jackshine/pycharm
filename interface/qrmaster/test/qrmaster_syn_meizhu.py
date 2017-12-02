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
    "mobile": "13326528030",
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


#同步美住客栈
def syn_community(s):
    s = syn_login_meizhu(s)
    resp_data = s.post(host_client + '/Home/Sync/getHotel').json()
    com_data = resp_data['data'][-1]
    params = {
        "hotelid": int(com_data["hotelentity_id"]),
        "hotelname": com_data["name"],
        "communityid": com_data["communityid"],
        "universaltime_id": int(com_data["universaltime_id"]),
        "communityname": com_data["name"]
    }
    data = {
        "hotels": '['+json.dumps(params, ensure_ascii=False)+']'
    }
    # print(data)
    syn_url = host_client + '/Home/Sync/syncCommunity'
    s.post(syn_url,data=data)

    # 同步房间
    hotel_data = {
        'hotelId': com_data["hotelentity_id"],
        'communityId': com_data["communityid"],
    }
    res = s.post(host_client + '/Home/Sync/getRoom', data=hotel_data).json()
    # print(res)
    room_dict = {}
    room_list = []
    room_str = ''
    for room in res['data'][0]['room']:
        room_dict['id']= room['id']
        room_dict['name']=room['name']
        room_list.append(room_dict)
        room_str=room_str+json.dumps(room_dict)+','
    add_room_data = {
        'hotelId': com_data["hotelentity_id"],
        'communityId':  com_data["communityid"],
        'builderName': '楼栋1',
        'builderNum': '1',
        'floorName': '楼层1',
        'floorNum': '1',
        'roomsAdd': '['+room_str[0:room_str.__len__()-1]+']',
    }
    print(add_room_data)
    response = s.post(host_client+'/Home/Sync/syncRoomAdd', data=add_room_data)
    print(response.text)


def syn_login_meizhu(s):
    sync_switch_url = host_client + '/Home/Sync/switchAccount'
    data = {
        'meizhu': '13326528030',
        'password': '111111b',
        'areaCode': '86'
    }
    s.post(sync_switch_url, data=data)
    return s

if __name__ == "__main__":
    s = requests.session()
    html_doc = s.get(link_client).text
    hash = get_hash(html_doc)
    handle_hash(data,hash)
    s.post(login_client_url, data=data)
    # 同步集群
    syn_community(s)
    # 切换到同步集群
    # s = change_commuity(s)








