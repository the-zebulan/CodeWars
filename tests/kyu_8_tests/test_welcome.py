import unittest

from katas.kyu_8.welcome import greet


class GreetTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(greet('english'), 'Welcome')

    def test_equal_2(self):
        self.assertEqual(greet('dutch'), 'Welkom')

    def test_equal_3(self):
        self.assertEqual(greet('IP_ADDRESS_INVALID'), 'Welcome')

    def test_equal_4(self):
        self.assertEqual(greet(''), 'Welcome')

    def test_equal_5(self):
        self.assertEqual(greet(2), 'Welcome')


if __name__ == '__main__':
    unittest.main()
