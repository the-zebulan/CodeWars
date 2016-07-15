import unittest

from katas.kyu_7.ghostbusters_whitespace_removal import ghostbusters


class GhostbustersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ghostbusters('Factor y'), 'Factory')

    def test_equals_2(self):
        self.assertEqual(ghostbusters('O  f fi ce'), 'Office')

    def test_equals_3(self):
        self.assertEqual(ghostbusters('BusStation'),
                         'You just wanted my autograph didn\'t you?')
