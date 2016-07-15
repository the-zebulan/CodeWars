import unittest

from katas.kyu_8.remove_the_time import shorten_to_date


class ShortenToDateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shorten_to_date('Monday February 2, 8pm'),
                         'Monday February 2')

    def test_equals_2(self):
        self.assertEqual(shorten_to_date('Tuesday May 29, 8pm'),
                         'Tuesday May 29')

    def test_equals_3(self):
        self.assertEqual(shorten_to_date('Wed September 1, 3am'),
                         'Wed September 1')

    def test_equals_4(self):
        self.assertEqual(shorten_to_date('Friday May 2, 9am'),
                         'Friday May 2')

    def test_equals_5(self):
        self.assertEqual(shorten_to_date('Tuesday January 29, 10pm'),
                         'Tuesday January 29')
