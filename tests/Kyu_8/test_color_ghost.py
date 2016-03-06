import unittest

from Kyu_8.color_ghost import COLORS, Ghost


class GhostTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertIn(Ghost().color, COLORS)


if __name__ == '__main__':
    unittest.main()
