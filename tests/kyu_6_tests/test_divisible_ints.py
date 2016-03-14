import unittest

from kyu_6.divisible_ints import get_count


class GetCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_count(123), 2)

    def test_equals_2(self):
        self.assertEqual(get_count(1230), 5)

    def test_equals_3(self):
        self.assertEqual(get_count(1), 0)

    def test_equals_4(self):
        self.assertEqual(get_count(1111111111), 25)


if __name__ == '__main__':
    unittest.main()
