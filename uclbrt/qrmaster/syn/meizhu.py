# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
import re
import time

class meizhu_class:
    def __init__(self,mz_client):


    def mz_add_hotel(mz_client_s):
        mz_client_s.post(mz_client + '/Home/Hotel/addHotel', data=mz_hotel_data)


    def mz_login_bpass(b):
        login_html = b.get(mz_bpass + '/index.php/Home/Public/login.html')
        soup = BeautifulSoup(login_html.text, "html.parser")
        vcode_src = mz_bpass + soup.find('img', id='imgcode')['src']
        while True:
            # 获取验证码
            vcode_img = b.get(vcode_src)
            with open('mz_vcode.png', 'wb') as fb:
                fb.write(vcode_img.content)
            vcode = input("输入验证码")
            bpass_login_data = {
                'username': 'changlian',
                'password': 'bbc69d27003568a7a94626ce4337bc9d',
                'vcode': vcode,
            }
            info = b.post(mz_bpass + '/Home/Public/checkLogin', data=bpass_login_data)
            if info.status_code == 200:
                break
        return b

    # 通过客栈审核
    def mz_bpass_pass_hotel(b, h_name):
        info = b.get(mz_bpass + "/index.php/Home/HotelApply/index.html")
        soup = BeautifulSoup(info.text, 'html.parser')

        td_list = soup.find('td', text=h_name).parent.find_all('td')
        h_info = json.loads(td_list[-1].button['data-json'], encoding='utf-8')
        mz_bpass_apply_data = {
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
        b.post(mz_bpass + '/Home/HotelApply/handle', data=mz_bpass_apply_data)

    # 美住添加房间
    def mz_add_room(s):
        info = s.get(mz_client + '/Home/RoomPage/index.html')
        soup = BeautifulSoup(info.text, 'html.parser')
        # 找到最后一个客栈的hotel_id
        hotel_id = soup.find('tbody', id='roomTypeHotelList').find_all('tr')[-1]['data-id']
        mz_room_data = {
            'room': '1,2,3,4,5',
            'hotel': hotel_id,
            'name': '单人间',
            'price': '100'
        }
        s.post(mz_client+'/Home/Room/addRoom',data=mz_room_data)
        params = {
            'hotel':hotel_id
        }



