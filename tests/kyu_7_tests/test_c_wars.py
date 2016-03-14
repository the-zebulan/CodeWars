import unittest

from katas.kyu_7.c_wars import initials


class InitialsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(initials('code wars'), 'C.Wars')

    def test_equals_2(self):
        self.assertEqual(initials('Barack Hussain obama'), 'B.H.Obama')


if __name__ == '__main__':
    unittest.main()
