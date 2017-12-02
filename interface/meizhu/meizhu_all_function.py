# encoding=utf-8
import requests
mz_client = 'http://115.29.142.212:8010'
index_url = mz_client + '/Home/BookPage/index.html'
login_url = mz_client + '/Home/Public/login'
add_hotel_url = mz_client + '/Home/Hotel/addHotel'

mz_bpass = 'http://115.29.142.212:8012'
mz_bpass_index_url = mz_bpass + '/index.php/Home/Public/login.html'
mz_bpass_login_url = mz_bpass + '/Home/Public/checkLogin'


login_data ={
    'mobile':'13326528030',
    'password':'111111b',
    'areaCode':'86',
}
def add_hotel(s):
    hotel_data = {
        'hotel':'阳江客栈-有为测试',
        'city':'320700',
        'district':'320704',
        'universalTime':'5'
    }
    s.post(add_hotel_url,data=hotel_data)


def login_bpass(b):
    b.get(mz_bpass_index_url)
    login_data = {
        'username':'changlian',
        'password':'bbc69d27003568a7a94626ce4337bc9d',
        'vcode':'',
    }
    info = b.post(mz_bpass_login_url,data=login_data)
    print(info.text)


if __name__ == "__main__":
    s = requests.session()
    s.get(index_url)
    resp = s.post(login_url,data=login_data)
    print(resp.text)
    # add_hotel(s)
    # 登陆bpass
    bpass = requests.session()
    login_bpass(bpass)
