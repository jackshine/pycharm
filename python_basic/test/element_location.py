# coding=utf-8
from selenium import webdriver
b = webdriver.Firefox()
b.get("http://115.29.142.212:8010/Home/BookPage/index.html")
b.maximize_window()
b.find_element_by_id("requestUsername").send_keys("13480251015")
b.find_element_by_id("requestPassword").send_keys("111111b")
b.find_element_by_id("requestSubmit").click()
b.implicitly_wait(5)
ele = b.find_element_by_link_text("统计")
ele.click()
b.back()
