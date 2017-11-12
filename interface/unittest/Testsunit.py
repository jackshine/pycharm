import unittest
from testcase import unittest_baidu_test
suite = unittest.TestSuite()
suite.addTest(BaiduTest('test_baidu'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))
if __name__ =="__main__":
    runner = unittest._TextTestRunner()
    runner.run(suite)
