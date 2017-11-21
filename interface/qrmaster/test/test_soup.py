from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(open('./company_verify_html.html','r',encoding='utf-8'),'html.parser')
#print(soup.find('table',id='questionTalbe'))
s_table = soup.find('table',id='questionTalbe')
a_list = s_table.find_all('a')
a_href = a_list[-1]['href']
print(a_href)