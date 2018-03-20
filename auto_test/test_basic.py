# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


def getHandler():
    browser = webdriver.Ie()
    return browser


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


def waitEle(b, xpath):
    locator = (By.XPATH, xpath)
    try:
        WebDriverWait(b, 30, 0.5).until(EC.visibility_of_element_located(locator))
    finally:
        print(locator)


def waitEleById(b, id):
    locator = (By.ID, id)
    try:
        WebDriverWait(b, 20, 0.5).until(EC.presence_of_element_located(locator))
    finally:
        print(locator)


# 办理入住
def checkIn(b):
    waitEle(b, "//*[@id='orderListBody']/tr[1]/td[4]/div")
    # 选择方格
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()

    # 输入姓名
    waitEle(b, "//*[@id='addOrderRoom']/table/tbody/tr[2]/td[1]/input")
    order_name_ele = b.find_element_by_xpath("//*[@id='addOrderRoom']/table/tbody/tr[2]/td[1]/input")
    order_name_ele.send_keys("lin")

    # 点击“提交订单”
    submit_Ele = b.find_element_by_xpath('//*[@id="submitBook"]')
    submit_Ele.click()
    time.sleep(1)

    # 确认弹出框（该订单没有收款，请确定）
    alt = b.switch_to_alert()
    alt.accept()

    waitEle(b,'//*[@id="initCheckIn"]')
    # 点击“办理入住”
    checkIn_Ele = b.find_element_by_xpath('//*[@id="initCheckIn"]')
    checkIn_Ele.click()
    time.sleep(1)

    # 点击“确认办理”
    confirm_Ele = b.find_element_by_xpath('//*[@id="checkInConfirm"]')
    confirm_Ele.click()
    time.sleep(1)

    # 点击“弹出框”
    continue_Alert = b.find_element_by_xpath('//*[@id="confirmEnterBtnL"]')
    continue_Alert.click()

    # 找“签发RF卡”元素
    waitEle(b, '//*[@id="orderInitContent"]/div[2]/div[1]/div[3]')
    issue_Ele = b.find_element_by_xpath('//*[@id="orderInitContent"]/div[2]/div[1]/div[3]')
    issue_Ele.click()

    # 签发RF卡
    waitEle(b, '//*[@id="orderRfContainer"]/div/div[2]/div[3]/div[1]')
    issue_button = b.find_element_by_xpath('//*[@id="orderRfContainer"]/div/div[2]/div[3]/div[1]')
    issue_button.click()

    # 点击X按钮
    # waitEle(b, '//*[@id="orderQRContent"]/div[1]/button')
    cancel_Ele = b.find_element_by_xpath('//*[@id="orderQRContent"]/div[1]/button')
    cancel_Ele.click()


def loginQRInn(b, acount_list, ele_id_dict):
    openUrl(b, acount_list['url'])

    Ele_list = findEle(b, ele_id_dict)
    sendInfo(acount_list, Ele_list)


# 已有订单办理入住
def checkInWithOrder(b):
    waitEle(b, "//*[@id='orderListBody']/tr[1]/td[4]/div")
    # 选择方格
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()

    # 点击“办理入住”
    # time.sleep(10)
    checkIn_Ele = b.find_element_by_xpath('//*[@id="initCheckIn"]')
    checkIn_Ele.click()
    time.sleep(1)

    # 点击“确认办理”
    confirm_Ele = b.find_element_by_xpath('//*[@id="checkInConfirm"]')
    confirm_Ele.click()
    time.sleep(1)

    # 点击“弹出框”
    continue_Alert = b.find_element_by_xpath('//*[@id="confirmEnterBtnL"]')
    continue_Alert.click()

    # 找“签发RF卡”元素
    time.sleep(5)
    # waitEle(b, '//*[@id="orderInitContent"]/div[2]/div[1]/div[3]')
    issue_Ele = b.find_element_by_xpath('//*[@id="orderInitContent"]/div[2]/div[1]/div[3]')
    issue_Ele.click()

    # 签发RF卡
    waitEle(b, '//*[@id="orderRfContainer"]/div/div[2]/div[3]/div[1]')
    issue_button = b.find_element_by_xpath('//*[@id="orderRfContainer"]/div/div[2]/div[3]/div[1]')
    issue_button.click()

    # 点击X按钮
    # waitEle(b, '//*[@id="orderQRContent"]/div[1]/button')
    cancel_Ele = b.find_element_by_xpath('//*[@id="orderQRContent"]/div[1]/button')
    cancel_Ele.click()

# 预定房间
def reserveOrder(b):

    waitEle(b, "//*[@id='orderListBody']/tr[1]/td[4]/div")
    # 选择方格
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()

    # 输入姓名
    waitEle(b, "//*[@id='addOrderRoom']/table/tbody/tr[2]/td[1]/input")
    order_name_ele = b.find_element_by_xpath("//*[@id='addOrderRoom']/table/tbody/tr[2]/td[1]/input")
    order_name_ele.send_keys("lin")

    # 点击“提交订单”
    submit_Ele = b.find_element_by_xpath('//*[@id="submitBook"]')
    submit_Ele.click()
    time.sleep(1)

    # 确认弹出框（该订单没有收款，请确定）
    alt = b.switch_to_alert()
    alt.accept()

    waitEle(b,'//*[@id="orderInitContent"]/div[1]/button')
    exitEle = b.find_element_by_xpath('//*[@id="orderInitContent"]/div[1]/button')
    exitEle.click()


def changeHotel(b):
    # 切换客栈
    waitEle(b, '//*[@id="doc-header-brand"]/div')
    change_Hotel_Ele = b.find_element_by_xpath('//*[@id="doc-header-brand"]')

    # 点击客栈
    change_Hotel_Ele.click()
    waitEle(b, '//*[@id="doc-header-brand-dropdown"]/div/li[4]/a')
    locationHotleEle = b.find_element_by_xpath('//*[@id="doc-header-brand-dropdown"]/div/li[4]/a')
    locationHotleEle.click()



def cancelOrder(b):
    waitEle(b, "//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele = b.find_element_by_xpath("//*[@id='orderListBody']/tr[1]/td[4]/div")
    select_square_Ele.click()

    # 点击“取消订单”
    waitEle(b,'//*[@id="initCancel"]')
    # time.sleep(5)
    cancel_order_Ele = b.find_element_by_xpath('//*[@id="initCancel"]')
    cancel_order_Ele.click()

    # time.sleep(5)
    waitEle(b,'//*[@id="initCancel"]')
    confirm_cancel_Ele = b.find_element_by_xpath('//*[@id="cancelOrderConfirm"]')
    confirm_cancel_Ele.click()

def controller(acount_list, ele_id_dict):
    b = getHandler()
    # loginQRInn(b, acount_list, ele_id_dict)

    openUrl(b, 'http://115.29.142.212:8010/Home/BookPage/index.html')
    changeHotel(b)
    checkIn(b)
    cancelOrder(b)
    reserveOrder(b)
    checkInWithOrder(b)
    cancelOrder(b)



if __name__ == "__main__":
    account_name = '18926368199'
    account_pwd = "111111b"
    url = "http://115.29.142.212:8010/login.html"
    acount_list = {"account_name": account_name, "account_pwd": account_pwd, "url": url}
    ele_id_dict = {"mobile_id": "requestUsername", "pwd_id": "requestPassword", "login_id": "requestSubmit"}
    # login_test(acount_list, ele_id_dict)
    controller(acount_list, ele_id_dict)
