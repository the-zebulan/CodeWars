import unittest

from katas.kyu_6.are_they_the_same import comp


class AreTheyTheSameTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(comp([121, 144, 19, 161, 19, 144, 19, 11],
                             [11 * 11, 121 * 121, 144 * 144, 19 * 19,
                              161 * 161, 19 * 19, 144 * 144, 19 * 19]))

    def test_true_2(self):
        self.assertTrue(comp([], []))

    def test_false(self):
        self.assertFalse(comp([], None))


if __name__ == '__main__':
    unittest.main()
