# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
b = webdriver.Firefox()
b.get("http://115.29.142.212:8010/Home/BookPage/index.html")
b.maximize_window()
b.find_element_by_id("requestUsername").send_keys("13480251015")
b.find_element_by_id("requestPassword").send_keys("111111b")
b.find_element_by_id("requestSubmit").click()
b.implicitly_wait(5)
ele = b.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/ul/li[2]/a/div")
ele.click()
ele = b.find_element_by_partial_link_text("家园客栈-测试")
ele.click()
#ActionChains(b).move_to_element(ele).perform()
#sub_ele = b.find_element_by_link_text("家园客栈-测试")
#sub_ele.click()