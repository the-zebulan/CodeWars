import unittest

from katas.kyu_7.shaving_the_beard import trim


class TrimTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(trim([['J', '|'], ['J', '|'], ['...', '|']]),
                         [['|', '|'], ['|', '|'], ['...', '...']])

    def test_equal_2(self):
        self.assertEqual(trim([
            ['J', '|', 'J'], ['J', '|', '|'], ['...', '|', 'J']
        ]), [['|', '|', '|'], ['|', '|', '|'], ['...', '...', '...']])

    def test_equal_3(self):
        self.assertEqual(trim([
            ['J', '|', 'J', 'J'], ['J', '|', '|', 'J'], ['...', '|', 'J', '|']
        ]), [['|', '|', '|', '|'], ['|', '|', '|', '|'],
             ['...', '...', '...', '...']])
