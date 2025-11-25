import unittest
import math
from calculator import add, minus, multiply, divide, percent, step, logarithm, factorial


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(0, 0), 0)

        self.assertNotEqual(add(1, 1), 3)

    def test_minus(self):
        self.assertEqual(minus(10, 4), 6)
        self.assertEqual(minus(0, 0), 0)
        self.assertEqual(minus(-10, -10), 0)

        self.assertNotEqual(minus(10, 9), 7)

    def test_multiply(self):
        self.assertEqual(multiply(7, 2), 14)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 3), -9)

        self.assertNotEqual(multiply(7, 20), 15)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(10, -2), -5)

        self.assertEqual(divide(5, 0), "Ошибка: деление на ноль!")
        self.assertNotEqual(divide(15, 3), 3)

    def test_percent(self):
        self.assertEqual(percent(200, 10), 20)
        self.assertEqual(percent(100, 50), 50)
        self.assertEqual(percent(10, 0), 0)

        self.assertNotEqual(percent(200, 15), 25)

    def test_step(self):
        self.assertEqual(step(2, 3), 8)
        self.assertEqual(step(5, 0), 1)
        self.assertEqual(step(0, 5), 0)

        self.assertNotEqual(step(2, 4), 9)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(math.e, math.e), 1)

        self.assertEqual(logarithm(-1), "Ошибка: логарифм не определён для неположительных чисел!")
        self.assertNotEqual(logarithm(200, 10), 3)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

        self.assertEqual(factorial(-1), "Ошибка: факториал не определён для отрицательных чисел!")
        self.assertNotEqual(factorial(4), 100)


if __name__ == '__main__':
    unittest.main()
