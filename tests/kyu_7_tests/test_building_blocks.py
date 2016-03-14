import unittest

from kyu_7.building_blocks import Block


class BlockTestCase(unittest.TestCase):
    def setUp(self):
        self.b = Block([2, 4, 6])
        self.b2 = Block([2, 2, 2])

    def test_equals(self):
        self.assertEqual(self.b.get_width(), 2)

    def test_equals_2(self):
        self.assertEqual(self.b.get_length(), 4)

    def test_equals_3(self):
        self.assertEqual(self.b.get_height(), 6)

    def test_equals_4(self):
        self.assertEqual(self.b.get_volume(), 48)

    def test_equals_5(self):
        self.assertEqual(self.b.get_surface_area(), 88)

    def test_equals_6(self):
        self.assertEqual(self.b2.get_width(), 2)

    def test_equals_7(self):
        self.assertEqual(self.b2.get_length(), 2)

    def test_equals_8(self):
        self.assertEqual(self.b2.get_height(), 2)

    def test_equals_9(self):
        self.assertEqual(self.b2.get_volume(), 8)

    def test_equals_10(self):
        self.assertEqual(self.b2.get_surface_area(), 24)


if __name__ == '__main__':
    unittest.main()
