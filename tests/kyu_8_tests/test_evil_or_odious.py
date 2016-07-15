import unittest

from katas.kyu_8.evil_or_odious import evil


class EvilOrOdiousTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(evil(1), 'It\'s Odious!')

    def test_equals_2(self):
        self.assertEqual(evil(2), 'It\'s Odious!')

    def test_equals_3(self):
        self.assertEqual(evil(3), 'It\'s Evil!')
