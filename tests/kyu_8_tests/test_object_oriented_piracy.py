import unittest

from kyu_8.object_oriented_piracy import Ship


class PirateShipTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(Ship(47, 5).is_worth_it())

    def test_false(self):
        self.assertFalse(Ship(15, 10).is_worth_it())

    def test_false_2(self):
        self.assertFalse(Ship(0, 0).is_worth_it())


if __name__ == '__main__':
    unittest.main()
