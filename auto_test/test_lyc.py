from selenium import webdriver
import time
import xlrd

username = ["18802094000", "18802094078", "1880209407", "18802094078"]
passwd = ["qq111111", "qqq111111", "qq111111", "qq111111"]
tip = ["用户不存在", "密码不正确", "手机号格式错误", ""]
url = "http://192.168.3.19:8090/login.html"
browser = webdriver.Firefox()
for x, y, z in zip(username, passwd, tip):
    time.sleep(10)
    browser.get(url)
    elem = browser.find_element_by_id("requestUsername")
    elem.send_keys(x)
    elem = browser.find_element_by_id("requestPassword")
    elem.send_keys(y)
    elem = browser.find_element_by_id("requestSubmit")
    elem.click()
    time.sleep(2)
    str = browser.find_element_by_id("login-tip").text
    print(str)
    if str == z:
        print("测试通过")
    else:
        print("ERRO", x, y, z)
