import unittest

from katas.beta.simple_beads_count import count_red_beads


class CountRedBeadsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(count_red_beads(1), 0)

    def test_equal_2(self):
        self.assertEqual(count_red_beads(3), 4)

    def test_equal_3(self):
        self.assertEqual(count_red_beads(5), 8)
