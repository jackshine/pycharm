#encoding=utf8
import unittest
def div(a,b):
    return a / b
class MyfirstTestCase(unittest.TestCase):
    def setUp(self):
        print 'run before every test'
    def tearDown(self):
        print 'run after every test'
    def test_1_div_1(self):
        print '1 div 1'
        self.assertEquals(div(1,1),1/1)
    def test_3_div_4(self):
        print '3 div 4'
        self.assertEquals(div(3, 4), 3 / 4)
    def test_3_div_0(self):
        print '3/0'
        self.assertRaises(ZeroDivisionError,3/0)
if __name__ == "__main__":
        unittest.main()

