# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import json

mz_client = 'http://115.29.142.212:8010'
index_url = mz_client + '/Home/BookPage/index.html'
login_url = mz_client + '/Home/Public/login'
add_hotel_url = mz_client + '/Home/Hotel/addHotel'

mz_bpass = 'http://115.29.142.212:8012'
mz_bpass_index_url = mz_bpass + '/index.php/Home/Public/login.html'
mz_bpass_login_url = mz_bpass + '/Home/Public/checkLogin'

login_data = {
    'mobile': '13326528030',
    'password': '111111b',
    'areaCode': '86',
}
hotel_data = {
    'city': '320700',
    'district': '320704',
    'universalTime': '5'
}


def add_hotel(s):
    s.post(add_hotel_url, data=hotel_data)


def login_bpass(b):
    login_html = b.get(mz_bpass_index_url)
    soup = BeautifulSoup(login_html.text, "html.parser")
    vcode_src = mz_bpass + soup.find('img', id='imgcode')['src']
    while True:
        # 获取验证码
        vcode_img = b.get(vcode_src)
        with open('vcode.png', 'wb') as fb:
            fb.write(vcode_img.content)
        vcode = input("输入验证码")
        login_data = {
            'username': 'changlian',
            'password': 'bbc69d27003568a7a94626ce4337bc9d',
            'vcode': vcode,
        }
        info = b.post(mz_bpass_login_url, data=login_data)
        print(info)
        if info.status_code == 200:
            break
    return b


# 通过客栈审核
def pass_hotel_apply(b, h_name):
    info = b.get(mz_bpass + "/index.php/Home/HotelApply/index.html")
    soup = BeautifulSoup(info.text, 'html.parser')
    td_list = soup.find('td', text=h_name).parent.find_all('td')
    h_info = json.loads(td_list[-1].button['data-json'], encoding='utf-8')
    apply_data = {
        'universalTime': h_info['universaltime_id'],
        'areacode': h_info['areacode'],
        'mobile': h_info['mobile'],
        'city': h_info['city_id'],
        'district': h_info['district_id'],
        'hotel': h_info['hotelname'],
        'id': h_info['id'],
        'username': h_info['username'],
        'kaitongDate': '1',
    }
    b.post(mz_bpass + '/Home/HotelApply/handle', data=apply_data)


def mz_add_room(s):
    info = s.get(mz_client + '/Home/RoomPage/index.html')
    soup = BeautifulSoup(info.text, 'html.parser')
    # 找到最后一个客栈的hotel_id
    hotel_id = soup.find('tbody', id='roomTypeHotelList').find_all('tr')[-1]['data-id']
    room_data = {
        'room': '1,2,3,4,5',
        'hotel': hotel_id,
        'name': '单人间',
        'price': '100'
    }
    print(room_data)
    res = s.post(mz_client+'/Home/Room/addRoom',data=room_data)
    print(res.text)
    params = {
        'hotel':hotel_id
    }


if __name__ == "__main__":
    h_name = input('输入客栈名称')
    # 佛山客栈-有为测试
    hotel_data['hotel'] = h_name.strip()
    s = requests.session()
    s.get(index_url)
    resp = s.post(login_url, data=login_data)
    print(resp.text)
    # add_hotel(s)
    # 登陆bpass
    # bpass = requests.session()
    # bpass = login_bpass(bpass)
    # 通过客栈认证
    # pass_hotel_apply(bpass,h_name)
    # 添加房间
    mz_add_room(s)
