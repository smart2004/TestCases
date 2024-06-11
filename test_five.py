# 5. Тестирование функций с помощью параметризации с использованием @parameterized:
# ```python
import unittest

from parameterized import parameterized

def subtract(x, y):
    return x - y

class TestSubtractFunction(unittest.TestCase):

    @parameterized.expand([
        (5, 3, 2),
        (10, 5, 5),
        (-5, 2, -7),
    ])

    def test_subtract_numbers(self, x, y, result):
        self.assertEqual(subtract(x, y), result)

if __name__ == '__main__':
    unittest.main()
