import unittest

from katas.kyu_6.salesmans_travel import travel


class TravelTestCase(unittest.TestCase):
    def setUp(self):
        self.test = '123 Main Street St. Louisville OH 43071,432 Main Long R' \
                    'oad St. Louisville OH 43071,786 High Street Pollocksvil' \
                    'le NY 56432'

    def test_equals(self):
        self.assertEqual(travel(self.test, 'OH 43071'),
                         'OH 43071:Main Street St. Louisville,Main Long Road'
                         ' St. Louisville/123,432')

    def test_equals_2(self):
        self.assertEqual(travel(self.test, 'NY 56432'),
                         'NY 56432:High Street Pollocksville/786')

    def test_equals_3(self):
        self.assertEqual(travel(self.test, 'NY 5643'), 'NY 5643:/')
