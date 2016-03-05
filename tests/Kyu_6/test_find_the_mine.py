import unittest

from Kyu_6.find_the_mine import mineLocation


class MineLocationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mineLocation([[1, 0], [0, 0]]), [0, 0])

    def test_equals_2(self):
        self.assertEqual(mineLocation(
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]]), [0, 0])

    def test_equals_3(self):
        self.assertEqual(mineLocation(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]), [2, 2])


if __name__ == '__main__':
    unittest.main()
