# 2. Тестирование функций с использованием assertTrue:
#```python
import unittest

def is_even(number):
    return number % 2 == 0

class TestIsEvenFunction(unittest.TestCase):

    def test_is_even_positive_number(self):
        self.assertTrue(is_even(2))

    def test_is_even_negative_number(self):
        self.assertTrue(not is_even(3))

if __name__ == '__main__':
    unittest.main()
    