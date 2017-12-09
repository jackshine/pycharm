# encoding=utf-8
import requests
from bs4 import BeautifulSoup
def get_hotel_id(tr):
    hotel_id = tr['data-id']
    if(hotel_id==''):
        hotel_id = get_hotel_id(tr.previous_sibling)
    else:
        hotel_id = tr['data-id']
    return hotel_id

if __name__ == '__main__':
    soup = BeautifulSoup(open('./room.html', 'r', encoding='utf-8'), 'html.parser')
    tr = soup.find('tbody', id='roomTypeHotelList').find_all('tr')[-1]
    hotel_id = tr['data-id']
    if (hotel_id == ''):
        tr = tr.previous_sibling.previous_sibling
        hotel_id  = get_hotel_id(tr)
        print(hotel_id)
    else:
        hotel_id = tr['data-id']


