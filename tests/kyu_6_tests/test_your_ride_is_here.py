import unittest

from katas.kyu_6.your_ride_is_here import ride


class RideTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ride('COMETQ', 'HVNGAT'), 'GO')

    def test_equals_2(self):
        self.assertEqual(ride('STARAB', 'USACO'), 'STAY')
