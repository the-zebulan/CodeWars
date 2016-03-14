import unittest

from Beta.herons_formula import heron


class HeronTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(heron(4, 13, 15), 24)

    def test_equals_2(self):
        self.assertEqual(heron(4, 3, 5), 6)

    def test_equals_3(self):
        self.assertEqual(heron(17, 25, 26), 204)


if __name__ == '__main__':
    unittest.main()
