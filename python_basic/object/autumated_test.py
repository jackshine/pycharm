#coding=utf-8
from selenium import webdriver
import time
url = "http://115.29.142.212:8010/Home/BookPage/index.html"
account_name = '13480251015'
accout_pwd = "111111a"
#打开浏览器
b = webdriver.Firefox()
b.get(url)
b.implicitly_wait(5)

#找到元素
name_Ele = b.find_element_by_id("requestUsername")
pwd_Ele = b.find_element_by_id("requestPassword")
login_Ele = b.find_element_by_id("requestSubmit")

#插入登录信息
name_Ele.send_keys(account_name)
pwd_Ele.send_keys(accout_pwd)
login_Ele.click()

#检查结果
time.sleep(5)
try:
    b.find_element_by_id("login-tip")
    print  b.find_element_by_id("login-tip").text
    print "error"
except:
    print "right"
