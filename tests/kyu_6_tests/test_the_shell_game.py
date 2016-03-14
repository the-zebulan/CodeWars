import unittest

from katas.kyu_6.the_shell_game import find_the_ball


class FindTheBallTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_the_ball(5, []), 5)

    def test_equals_2(self):
        self.assertEqual(find_the_ball(0, [(0, 1), (2, 1), (0, 1)]), 2)


if __name__ == '__main__':
    unittest.main()
