import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(19,23),42)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(10,9), 1)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(-88,100), -188)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(1, 50), 50)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)

    def test_div1(self):
        self.assertEqual(self.calc.divide(50, 1), 50)

    def test_div2(self):
        self.assertEqual(self.calc.divide(125, 5), 25)

    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(100, 1), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()