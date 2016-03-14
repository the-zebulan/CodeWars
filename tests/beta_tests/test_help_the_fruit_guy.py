import unittest

from Beta.help_the_fruit_guy import remove_rotten


class RemoveRottenTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove_rotten(
            ['rottenApple', 'rottenBanana', 'rottenApple', 'rottenPineapple',
             'rottenKiwi']), ['apple', 'banana', 'apple', 'pineapple', 'kiwi'])

    def test_equals_2(self):
        self.assertEqual(remove_rotten([]), [])


if __name__ == '__main__':
    unittest.main()
