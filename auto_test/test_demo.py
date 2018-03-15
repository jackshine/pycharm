# coding=utf-8
from selenium import webdriver
import time


def getHandler():
    return webdriver.Firefox()


def findEle(b):
    # 找到元素
    name_Ele = b.find_element_by_class_name("order-item-td without-order highlight")
    name_Ele.click()


def openUrl(url):
    b = webdriver.Firefox()
    b.get(url)
    findEle(b)


if __name__ == "__main__":
    url = "http://115.29.142.212:8010/Home/BookPage/index.html"
    openUrl(url)
