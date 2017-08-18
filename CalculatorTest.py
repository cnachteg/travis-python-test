import unittest
from Calculator import Calculator
import math
import sys

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_add(self):
        arg1 = 5
        arg2 = 3
        self.assertEqual(Calculator.add(arg1,arg2),arg1+arg2)

    def test_sub(self):
        arg1 = 5
        arg2 = 3
        self.assertEqual(Calculator.sub(arg1,arg2),arg1-arg2)

    def test_mul(self):
        arg1 = 5
        arg2 = 3
        self.assertEqual(Calculator.mul(arg1,arg2),arg1*arg2)

    def test_div(self):
        arg1 = 5
        arg2 = 3
        self.assertEqual(Calculator.div(arg1,arg2),arg1/arg2)

    def test_sqrt(self):
        arg1 = 25
        self.assertEqual(Calculator.sqrt(arg1),math.sqrt(arg1))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    test_runner = unittest.TextTestRunner(verbosity=2).run(test_suite)
    ret = not test_runner.wasSuccessful()
    sys.exit(ret) 
    """ 
    Travis build status depends on exit code.
    Without the last line the exit code of the program is 0 even if the tests fail.
    """




