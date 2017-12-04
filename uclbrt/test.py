#incoding=utf-8
import requests,time
from bs4 import BeautifulSoup
begintime = time.time()
headers={
    "Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Accept":"*/*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":"XMLHttpRequest",
    "Connection":"keep-alive"
}


login_url=r'https://www.zhihu.com/login/email'

html_txt = requests.get(login_url,verify=False).text
html_soup = BeautifulSoup(html_txt,'lxml')
xsrf = html_soup.find("input",{"name":"_xsrf"})['value']

#print xsrf
#print html_txt
s = requests.session()

url_data={
    "_xsrf":xsrf,
    "email":"******",
    "password":"********",
    'remember_me':'true'
}

s_login=s.post(login_url,data=url_data,headers=headers,verify=False)
print s_login.text

endtime = time.time()
usetime =  endtime - begintime
print "执行脚本总用时 %s 秒" % usetime

#print s.get('https://www.zhihu.com',verify=False).text