# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
b = webdriver.Firefox()
b.get("https://www.hao123.com/")
b.maximize_window()
ele = b.find_element_by_css_selector("div span .login__hongbao-text")
ele.click()
b.implicitly_wait(5)
ele = b.find_element_by_id("TANGRAM__PSP_10__userName")
ele.send_keys("yjlyw020150@163.com")
ele = b.find_element_by_id("TANGRAM__PSP_10__password")
ele.send_keys("yjlyw199241")
ele = b.find_element_by_id("TANGRAM__PSP_10__submit")
ele.click()
b.implicitly_wait(5)
ele = b.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[4]/div[1]/div/div/a/span")
ActionChains(b).move_to_element(ele).perform()
