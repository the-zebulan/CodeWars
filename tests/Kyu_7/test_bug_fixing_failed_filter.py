import unittest

from Kyu_7.bug_fixing_failed_filter import filter_numbers


class FilterNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(filter_numbers('test123'), 'test')

    def test_equals_2(self):
        self.assertEqual(filter_numbers('a1b2c3'), 'abc')

    def test_equals_3(self):
        self.assertEqual(filter_numbers('aa1bb2cc3dd'), 'aabbccdd')


if __name__ == '__main__':
    unittest.main()
