# coding=utf-8
from selenium import webdriver
import unittest,time

class youdao_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://fanyi.baidu.com"
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("baidu_translate_input").clear()
        driver.find_element_by_id("baidu_translate_input").send_keys("你好")
        driver.find_element_by_id("translate-button").click()
        time.sleep(5)
        title = driver.page_source
        print(title)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()