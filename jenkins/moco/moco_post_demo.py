#encoding=utf8
import requests
import unittest
class test2(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    def test_aa(self):
        self.data = requests.post("http://127.0.0.1:16823/posts").json()
        print(self.data)
if __name__ == "__main__":
    a = test2()
    a.test_aa()