import unittest

from kyu_8.regular_ball_super_ball import Ball


class BallTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Ball().ball_type, 'regular')

    def test_equals_2(self):
        self.assertEqual(Ball('super').ball_type, 'super')


if __name__ == '__main__':
    unittest.main()
