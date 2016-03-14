import unittest

from beta.who_ate_the_cookie import cookie


class CookieTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(cookie('Ryan'),
                         'Who ate the last cookie? It was Zach!')

    def test_equals_2(self):
        self.assertEqual(cookie(2.3),
                         'Who ate the last cookie? It was Monica!')

    def test_equals_3(self):
        self.assertEqual(cookie(26),
                         'Who ate the last cookie? It was Monica!')

    def test_equals_4(self):
        self.assertEqual(cookie(True),
                         'Who ate the last cookie? It was the dog!')


if __name__ == '__main__':
    unittest.main()
