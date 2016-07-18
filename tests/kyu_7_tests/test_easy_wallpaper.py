import unittest

from katas.kyu_7.easy_wallpaper import wallpaper


class WallpaperTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(wallpaper(4, 3.5, 3), 'ten')

    def test_equal_2(self):
        self.assertEqual(wallpaper(6.3, 4.5, 3.29), 'sixteen')

    def test_equal_3(self):
        self.assertEqual(wallpaper(7.8, 2.9, 3.29), 'sixteen')

    def test_equal_4(self):
        self.assertEqual(wallpaper(6.3, 5.8, 3.13), 'seventeen')

    def test_equal_5(self):
        self.assertEqual(wallpaper(6.1, 6.7, 2.81), 'sixteen')

    def test_equal_6(self):
        self.assertEqual(wallpaper(0, 5.8, 3), 'zero')

    def test_equal_7(self):
        self.assertEqual(wallpaper(5.8, 0, 3), 'zero')
