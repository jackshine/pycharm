# encoding=utf-8
from bs4 import BeautifulSoup
import json
class MeizhuClass:
    mz_client = ''
    mz_bpass = ''

    def __init__(self,mz_client,mz_bpass):
        self.mz_client = mz_client
        self.mz_bpass = mz_bpass


    def mz_add_hotel(self, mz_client_s,mz_hotel_data):
        s = mz_client_s.post(self.mz_client + '/Home/Hotel/addHotel', data=mz_hotel_data)
        print(s.text)



    def mz_login_bpass(self,b,bpass_login_data):
        login_html = b.get(self.mz_bpass + '/index.php/Home/Public/login.html')
        soup = BeautifulSoup(login_html.text, "html.parser")
        vcode_src = self.mz_bpass + soup.find('img', id='imgcode')['src']
        while True:
            # 获取验证码
            vcode_img = b.get(vcode_src)
            with open('mz_vcode.png', 'wb') as fb:
                fb.write(vcode_img.content)
            vcode = input("请输入验证码：")
            bpass_login_data['vcode'] = vcode,
            info = b.post(self.mz_bpass + '/Home/Public/checkLogin', data=bpass_login_data)
            if info.status_code == 200:
                break
        return b

    # 通过客栈审核
    def mz_bpass_pass_hotel(self, b, h_name):
        info = b.get(self.mz_bpass + "/index.php/Home/HotelApply/index.html")
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
        b.post(self.mz_bpass + '/Home/HotelApply/handle', data=mz_bpass_apply_data)

    # 美住添加房间
    def mz_add_room(self, s,mz_room_data):
        info = s.get(self.mz_client + '/Home/RoomPage/index.html')
        soup = BeautifulSoup(info.text, 'html.parser')
        # 找到最后一个客栈的hotel_id
        hotel_id = soup.find('tbody', id='roomTypeHotelList').find_all('tr')[-1]['data-id']
        mz_room_data['hotel'] = hotel_id
        s.post(self.mz_client+'/Home/Room/addRoom',data=mz_room_data)



