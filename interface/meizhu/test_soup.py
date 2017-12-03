# encoding=utf-8
from bs4 import BeautifulSoup
import json
soup = BeautifulSoup(open('./apply.html', 'r', encoding='utf-8'), 'html.parser')
td_list = soup.find('td', text='佛山客栈-有为测试').parent.find_all('td')
h_info = json.loads(td_list[-1].button['data-json'],encoding='utf-8')
apply_data = {
    'universalTime': h_info['universaltime_id'],
    'areacode': h_info['areacode'],
    'mobile': ['mobile'],
    'city': h_info['city_id'],
    'district': h_info['district_id'],
    'hotel': h_info['hotelname'],
    'id': h_info['id'],
    'username': h_info['username'],
    'kaitongDate': '1',
}
print(apply_data)
