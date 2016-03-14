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


if __name__ == '__main__':
    unittest.main()
