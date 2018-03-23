# coding=utf-8
from selenium import webdriver
import time


def getHandler():
    return webdriver.Ie()


def openUrl(b, url):
    b.get(url)


def findEle(b, ele_id_list):
    # 找到元素
    name_Ele = b.find_element_by_id(ele_id_list['mobile_id'])
    pwd_Ele = b.find_element_by_id(ele_id_list['pwd_id'])
    login_Ele = b.find_element_by_id(ele_id_list['login_id'])
    Ele_list = []
    Ele_list.append(name_Ele)
    Ele_list.append(pwd_Ele)
    Ele_list.append(login_Ele)

    return Ele_list


def sendInfo(acount_list, Ele_list):
    list_key = ['account_name', 'account_pwd']
    for i in range(len(list_key)):
        Ele_list[i].send_keys("")
        Ele_list[i].send_keys(acount_list[list_key[i]])
    Ele_list[len(list_key)].click()


# 办理入住
def issueCard(b):
    # 选择方格
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()
    time.sleep(6)
    # 输入姓名
    order_name_ele = b.find_element_by_xpath("//*[@id='addOrderRoom']/table/tbody/tr[2]/td[1]/input")
    order_name_ele.send_keys("lin")
    # 点击“提交订单”
    submit_Ele = b.find_element_by_xpath('//*[@id="submitBook"]')
    submit_Ele.click()
    alt = b.switch_to_alert()
    time.sleep(1)
    alt.accept()
    time.sleep(1)
    # 点击“确认办理入住”
    checkIn_Ele = b.find_element_by_xpath('//*[@id="initCheckIn"]')
    checkIn_Ele.click()
    time.sleep(1)
    confirm_Ele = b.find_element_by_xpath('//*[@id="checkInConfirm"]')
    confirm_Ele.click()
    time.sleep(1)
    # 点击“弹出框”
    continue_Alert = b.find_element_by_xpath('//*[@id="confirmEnterBtnL"]')
    continue_Alert.click()
    time.sleep(1)
    issue_Ele = b.find_element_by_xpath('//*[@id="orderInitContent"]/div[2]/div[1]/div[3]')
    issue_Ele.click()
    time.sleep(2)
    # 签发RF卡
    issue_button = b.find_element_by_xpath('//*[@id="orderRfContainer"]/div/div[2]/div[3]/div[1]')
    issue_button.click()
    time.sleep(5)
    # 点击X按钮
    cancel_Ele = b.find_element_by_xpath('//*[@id="orderQRContent"]/div[1]/button')
    cancel_Ele.click()


def cancelOrder(b):
    time.sleep(5)
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()
    time.sleep(5)
    # 点击“取消订单”
    cancel_order_Ele = b.find_element_by_xpath('//*[@id="initCancel"]')
    cancel_order_Ele.click()
    confirm_cancel_Ele = b.find_element_by_xpath('//*[@id="cancelOrderConfirm"]')
    confirm_cancel_Ele.click()



def changeHotel(b):
    # 切换客栈
    time.sleep(10)
    change_Hotel_Ele = b.find_element_by_xpath('//*[@id="doc-header-brand"]')
    # 点击客栈
    change_Hotel_Ele.click()
    time.sleep(4)
    location_Hotle_Ele = b.find_element_by_xpath('//*[@id="doc-header-brand-dropdown"]/div/li[4]/a')
    location_Hotle_Ele.click()
    time.sleep(2)


def controller(acount_list, ele_id_dict):
    b = getHandler()
    openUrl(b, acount_list['url'])
    changeHotel(b)
    issueCard(b)


if __name__ == "__main__":
    account_name = '18926368199'
    account_pwd = "111111b"
    url = "http://115.29.142.212:8010/login.html"
    acount_list = {"account_name": account_name, "account_pwd": account_pwd, "url": url}
    ele_id_dict = {"mobile_id": "requestUsername", "pwd_id": "requestPassword", "login_id": "requestSubmit"}
    # login_test(acount_list, ele_id_dict)
    controller(acount_list, ele_id_dict)
