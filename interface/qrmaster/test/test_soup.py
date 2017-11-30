from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(open('./table.html','r',encoding='utf-8'),'html.parser')
#print(soup.find('table',id='questionTalbe'))
table = soup.find('table',id='roomTable')
#print(table.tbody.tr.next_sibling.next_sibling)
tr_list = table.tbody.find_all('tr')
num = 0
for i in tr_list:
    num += 1
print(num)