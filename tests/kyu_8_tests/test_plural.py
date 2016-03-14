import unittest

from kyu_8.plural import plural


class PluralTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(plural(0))

    def test_true_2(self):
        self.assertTrue(plural(0.5))

    def test_true_3(self):
        self.assertTrue(plural(100))

    def test_false(self):
        self.assertFalse(plural(1))


if __name__ == '__main__':
    unittest.main()
