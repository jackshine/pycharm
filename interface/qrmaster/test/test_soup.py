from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(open('./table.html','r',encoding='utf-8'),'html.parser')
#print(soup.find('table',id='questionTalbe'))
div_tag = soup.find('div',id='doc-center-page')
#print(table.tbody.tr.next_sibling.next_sibling)
page_url = div_tag.find_all('a')
count = page_url.__len__()
page_url = page_url[:-count:-1]
page_url_list = []
for i in page_url:
    page_url_list.append(i['href'])
print(page_url_list)


