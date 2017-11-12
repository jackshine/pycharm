# coding=utf-8
from selenium import webdriver
import unittest,time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("eeee")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        print(title)
        self.assertEqual(title,u"unittest_百度搜索")
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()