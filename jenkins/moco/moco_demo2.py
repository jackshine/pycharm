#encoding=utf8
import requests
import unittest
url = "http://127.0.0.1:16823/posts"
class test2(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    def test_aa(self,url):
        print(url)
        self.data = requests.post(url,json={"title":"123","content":"333"})
        print(self.data.text)
if __name__ == "__main__":
    a = test2()
    a.test_aa(url)