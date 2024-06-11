# 4. Тестирование классов с использованием setUp и tearDown:
# ```python
import unittest

class Calculator:

    def add(self, x, y):
        return x + y

class TestCalculatorClass(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        del self.calculator

    def test_add_positive_numbers(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
