import unittest

from katas.beta.yes_no_yes_no import yes_no


class YesNoTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(yes_no([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         [1, 3, 5, 7, 9, 2, 6, 10, 8, 4])

    def test_equal_2(self):
        self.assertEqual(yes_no(['this', 'code', 'is', 'right', 'the']),
                         ['this', 'is', 'the', 'right', 'code'])

    def test_equal_3(self):
        self.assertEqual(yes_no([]), [])

    def test_equal_4(self):
        self.assertEqual(yes_no(['a']), ['a'])

    def test_equal_5(self):
        self.assertEqual(yes_no(['a', 'b']), ['a', 'b'])


if __name__ == '__main__':
    unittest.main()
