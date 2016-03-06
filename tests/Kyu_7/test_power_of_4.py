import unittest

from Kyu_7.power_of_4 import powerof4


class PowerOfFourTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(powerof4(1024))

    def test_true_2(self):
        self.assertTrue(powerof4(64))

    def test_true_3(self):
        self.assertTrue(powerof4(1))

    def test_false(self):
        self.assertFalse(powerof4(102))

    def test_false_2(self):
        self.assertFalse(powerof4(25))

    def test_false_3(self):
        self.assertFalse(powerof4(-25))

    def test_false_4(self):
        self.assertFalse(powerof4('aa'))

    def test_false_5(self):
        self.assertFalse(powerof4(True))


if __name__ == '__main__':
    unittest.main()
