import unittest

from katas.kyu_7.reverse_it import reverse_it


class ReverseItTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse_it('Hello'), 'olleH')

    def test_equals_2(self):
        self.assertEqual(reverse_it(314159), 951413)

    def test_equals_3(self):
        self.assertEqual(reverse_it('314159'), '951413')

    def test_equals_4(self):
        self.assertEqual(reverse_it('123.123'), '321.321')

    def test_equal_5(self):
        func = lambda: 1
        self.assertEqual(reverse_it(func), func)

    def test_equal_6(self):
        self.assertEqual(reverse_it([1, 2, 3, 4]), [1, 2, 3, 4])
