import unittest

from katas.kyu_7.grid_blast import fire


class FireTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(fire(0, 0), 'top left')

    def test_equals_2(self):
        self.assertEqual(fire(1, 2), 'bottom middle')

    def test_equals_3(self):
        self.assertEqual(fire(1, 1), 'center')
