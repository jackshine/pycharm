import unittest
import sys,os
sys.path.append( os.path.dirname(os.path.realpath(__file__))  )
print( os.path.dirname(os.path.realpath(__file__)))
from .test_mathfunc import *

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"),TestMathFunc("test_divide")]
    # suite.addTests(tests)
    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)