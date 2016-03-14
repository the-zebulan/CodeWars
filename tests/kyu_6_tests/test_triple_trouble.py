import unittest

from kyu_6.triple_trouble import triple_double


class TripleTroubleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(triple_double(451999277, 41177722899), 1)

    def test_equals_2(self):
        self.assertEqual(triple_double(1222345, 12345), 0)

    def test_equals_3(self):
        self.assertEqual(triple_double(12345, 12345), 0)

    def test_equals_4(self):
        self.assertEqual(triple_double(666789, 12345667), 1)

    def test_equals_5(self):
        self.assertEqual(triple_double(10560002, 100), 1)


if __name__ == '__main__':
    unittest.main()
