import unittest

from katas.kyu_7.self_descriptive_numbers import self_descriptive


class SelfDescriptiveNumbersTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(self_descriptive(21200))

    def test_true_2(self):
        self.assertTrue(self_descriptive(3211000))

    def test_true_3(self):
        self.assertTrue(self_descriptive(42101000))

    def test_true_4(self):
        self.assertTrue(self_descriptive(1210))

    def test_true_5(self):
        self.assertTrue(self_descriptive(2020))

    def test_true_6(self):
        self.assertTrue(self_descriptive(6210001000))

    def test_false(self):
        self.assertFalse(self_descriptive(21230))

    def test_false_2(self):
        self.assertFalse(self_descriptive(11200))

    def test_false_3(self):
        self.assertFalse(self_descriptive(51120111))

    def test_false_4(self):
        self.assertFalse(self_descriptive(11201))


if __name__ == '__main__':
    unittest.main()
