import unittest

from katas.kyu_7.boiled_eggs import cooking_time


class CookingTimeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(cooking_time(0), 0)

    def test_equals_2(self):
        self.assertEqual(cooking_time(5), 5)

    def test_equals_3(self):
        self.assertEqual(cooking_time(10), 10)


if __name__ == '__main__':
    unittest.main()
