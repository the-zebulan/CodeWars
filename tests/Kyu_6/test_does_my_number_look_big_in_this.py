import unittest

from Kyu_6.does_my_number_look_big_in_this import narcissistic


class NarcissisticTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(narcissistic(7))

    def test_true_2(self):
        self.assertTrue(narcissistic(371))

    def test_false(self):
        self.assertFalse(narcissistic(122))

    def test_false_2(self):
        self.assertFalse(narcissistic(4887))


if __name__ == '__main__':
    unittest.main()
