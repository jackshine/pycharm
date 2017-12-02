# encoding=utf-8
import requests
meizhu_client = 'http://115.29.142.212:8010'
index_url = meizhu_client + '/Home/BookPage/index.html'
login_url = meizhu_client + '/Home/Public/login'
add_hotel_url = meizhu_client + '/Home/Hotel/addHotel'

meizhu_bpass = 'http://115.29.142.212:8012/'
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

if __name__ == "__main__":
    s = requests.session()
    s.get(index_url)
    resp = s.post(login_url,data=login_data)
    print(resp.text)
    add_hotel(s)
