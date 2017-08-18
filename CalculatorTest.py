import unittest
import Calculator
import math

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_sum():
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.sum(arg1,arg2),arg1+arg2)

    def test_sub():
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.sub(arg1,arg2),arg1-arg2)

    def test_mul():
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.mul(arg1,arg2),arg1*arg2)

    def test_div():
        arg1 = 5
        arg2 = 3
        assertEqual(Calculator.div(arg1,arg2),arg1+arg2)

    def test_sqrt():
        arg1 = 25
        assertEqual(Calculator.sqrt(arg1),math.sqrt(arg1))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)




