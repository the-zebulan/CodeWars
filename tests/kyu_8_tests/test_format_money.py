import unittest

from katas.kyu_8.format_money import format_money


class FormatMoneyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(format_money(39.99), '$39.99')


if __name__ == '__main__':
    unittest.main()
