import unittest

from Beta.food_combinations import actually_really_good


class ActuallyReallyGoodTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(actually_really_good([]),
                         'You know what\'s actually really good? Nothing!')

    def test_equals_2(self):
        self.assertEqual(actually_really_good(['Peanut butter']),
                         'You know what\'s actually really good? Peanut '
                         'butter and more peanut butter.')


if __name__ == '__main__':
    unittest.main()
