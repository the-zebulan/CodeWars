import unittest

from katas.beta.mtv_cribs import my_crib


class MyCribTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(my_crib(1), ' /\\ \n/__\\\n|__|')

    def test_equal_2(self):
        self.assertEqual(
            my_crib(2), '  /\\  \n /  \\ \n/____\\\n|    |\n|____|')

    def test_equal_3(self):
        self.assertEqual(my_crib(3), '   /\\   \n  /  \\  \n /    \\ \n'
                                     '/______\\\n|      |\n|      |\n|______|')
