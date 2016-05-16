import unittest

from katas.beta.another_one_down import check


class CheckTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(check(123), 'Input is not a string')

    def test_is_none_1(self):
        self.assertIsNone(check('my_string'))


if __name__ == '__main__':
    unittest.main()
