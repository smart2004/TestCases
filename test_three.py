#3. Тестирование исключений с использованием assertRaises:
# ```python
import unittest

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class TestDivideFunction(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

if __name__ == '__main__':
    unittest.main()
    