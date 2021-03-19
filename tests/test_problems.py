import unittest
from coin_flips import coin_flips
from factorial import factorial
from fib import fib
from find_max import find_max


class TestCalc(unittest.TestCase):

    def test_coin_flips(self):
        self.answer_two = ['HHHH', 'THHH', 'HTHH', 'TTHH', 'HHTH', 'THTH', 'HTTH', 'TTTH', 'HHHT', 'THHT', 'HTHT', 'TTHT', 'HHTT', 'THTT', 'HTTT', 'TTTT']
        self.assertEqual(coin_flips(2), ['HH', 'TH', 'HT', 'TT'])
        self.assertEqual(coin_flips(4), self.answer_two)
        self.assertEqual(coin_flips(1), ['H', 'T'])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_fib(self):
        self.assertEqual(fib(-1), 0)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(20), 6765)

    def test_find_max(self):
        self.assertEqual(find_max([1, 4, 45, 6, -50, 10, 2]), 45)
        
    # def test_pretty_print(self):
    #     self.assertEqual(calc.multiply(10, 5), 50)
    #     self.assertEqual(calc.multiply(100, 1), 100)
    #     self.assertEqual(calc.multiply(-88, 88), -7744)
    #     self.assertEqual(calc.multiply(2, 2), 4)
        
    # def test_reverse(self):
    #     self.assertEqual(calc.multiply(10, 5), 50)
    #     self.assertEqual(calc.multiply(100, 1), 100)
    #     self.assertEqual(calc.multiply(-88, 88), -7744)
    #     self.assertEqual(calc.multiply(2, 2), 4)
        
        
if __name__ == '__main__':
    unittest.main()