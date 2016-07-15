import unittest

from katas.kyu_4.strip_url_params import strip_url_params


class StripURLParamsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(strip_url_params('www.codewars.com?a=1&b=2&a=1&b=3'),
                         'www.codewars.com?a=1&b=2')

    def test_equals_2(self):
        self.assertEqual(strip_url_params('www.codewars.com?a=1&b=2&a=1&b=3',
                                          ['b']), 'www.codewars.com?a=1')

    def test_equals_3(self):
        self.assertEqual(strip_url_params('www.codewars.com?a=1&b=2&a=2'),
                         'www.codewars.com?a=1&b=2')

    def test_equals_4(self):
        self.assertEqual(strip_url_params('www.codewars.com?a=1&b=2&a=2',
                                          ['b']), 'www.codewars.com?a=1')

    def test_equals_5(self):
        self.assertEqual(strip_url_params('www.codewars.com', ['b']),
                         'www.codewars.com')
