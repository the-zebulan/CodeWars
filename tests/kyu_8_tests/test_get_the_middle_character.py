import unittest

from katas.kyu_8.get_the_middle_character import get_middle


class GetMiddleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_middle('test'), 'es')

    def test_equals_2(self):
        self.assertEqual(get_middle('testing'), 't')

    def test_equals_3(self):
        self.assertEqual(get_middle('middle'), 'dd')

    def test_equals_4(self):
        self.assertEqual(get_middle('A'), 'A')

    def test_equals_5(self):
        self.assertEqual(get_middle('of'), 'of')


if __name__ == '__main__':
    unittest.main()
