import unittest
from calculator import *

# https://github.com/elau967/lab11-EL-SK.git
# Partner 1: Eric Lau
# Partner 2: Simon Kareng

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
# 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        self.assertEqual(mul(5, 4), 20)
        self.assertEqual(mul(0.25, 10), 2.5)
        self.assertEqual(mul(3, 0), 0)

    def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(div(1, 5), 5)
        self.assertEqual(div(2, 20), 10)
        self.assertEqual(div(3, 3), 1)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self):
        self.assertEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(math.e ** 2, math.e), 2)# 3 assertions
    #     fill in code

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)
        # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(5, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
    #     fill in code

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code

        with self.assertRaises(ValueError):
            square_root(-2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()