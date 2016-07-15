import unittest

from katas.kyu_8.jennys_secret_msg import greet


class GreetTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greet('James'), 'Hello, James!')

    def test_equals_2(self):
        self.assertEqual(greet('Johnny'), 'Hello, my love!')
