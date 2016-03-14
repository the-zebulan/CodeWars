import unittest

from katas.kyu_7.power_of_two import power_of_two


class PowerOfTwoTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(power_of_two(1))

    def test_true_2(self):
        self.assertTrue(power_of_two(2))

    def test_true_3(self):
        self.assertTrue(power_of_two(4096))

    def test_true_4(self):
        self.assertTrue(power_of_two(33554432))

    def test_true_5(self):
        self.assertTrue(power_of_two(8388608))

    def test_true_6(self):
        self.assertTrue(power_of_two(16777216))

    def test_true_7(self):
        self.assertTrue(power_of_two(8388608))

    def test_true_8(self):
        self.assertTrue(power_of_two(4194304))

    def test_false(self):
        self.assertFalse(power_of_two(5))

    def test_false_2(self):
        self.assertFalse(power_of_two(4194305))

    def test_false_3(self):
        self.assertFalse(power_of_two(16777217))

    def test_false_4(self):
        self.assertFalse(power_of_two(16777215))


if __name__ == '__main__':
    unittest.main()
