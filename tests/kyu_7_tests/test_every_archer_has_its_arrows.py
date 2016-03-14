import unittest

from Kyu_7.every_archer_has_its_arrows import archers_ready


class ArchersReadyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(archers_ready([5, 6, 7, 8]))

    def test_false(self):
        self.assertFalse(archers_ready([]))

    def test_false_2(self):
        self.assertFalse(archers_ready([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
