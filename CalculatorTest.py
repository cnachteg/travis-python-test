import unittest
import Calculator
import math

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_sum(self):
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.sum(arg1,arg2),arg1+arg2)

    def test_sub(self):
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.sub(arg1,arg2),arg1-arg2)

    def test_mul(self):
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.mul(arg1,arg2),arg1*arg2)

    def test_div(self):
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.div(arg1,arg2),arg1+arg2)

    def test_sqrt(self):
        arg1 = 25
        assertEqual(Calculator.sqrt(arg1),math.sqrt(arg1))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    test_runner = unittest.TextTestRunner(verbosity=2).run(test_suite)
    ret = not test_runner.wasSuccessful()
    sys.exit(ret) 
    """ 
    Travis build status depends on exit code.
    Without the last line the exit code of the program is 0 even if the tests fail.
    """




