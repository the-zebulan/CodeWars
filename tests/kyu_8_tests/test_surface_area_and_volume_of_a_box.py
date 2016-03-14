import unittest

from katas.kyu_8.surface_area_and_volume_of_a_box import get_size


class GetSizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_size(4, 2, 6), [88, 48])

    def test_equals_2(self):
        self.assertEqual(get_size(1, 1, 1), [6, 1])

    def test_equals_3(self):
        self.assertEqual(get_size(1, 2, 1), [10, 2])

    def test_equals_4(self):
        self.assertEqual(get_size(1, 2, 2), [16, 4])

    def test_equals_5(self):
        self.assertEqual(get_size(10, 10, 10), [600, 1000])


if __name__ == '__main__':
    unittest.main()
