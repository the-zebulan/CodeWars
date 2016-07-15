import unittest

from katas.kyu_8.squash_the_bugs import find_longest


class SquashTheBugsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_longest(
            'The quick white fox jumped around the massive dog'
            ), 7
        )

    def test_equals_2(self):
        self.assertEqual(find_longest('Take me to tinseltown with you'), 10)

    def test_equals_3(self):
        self.assertEqual(find_longest('Sausage chops'), 7)

    def test_equals_4(self):
        self.assertEqual(
            find_longest('Wind your body and wiggle your belly'), 6
        )

    def test_equals_5(self):
        self.assertEqual(find_longest('Lets all go on holiday'), 7)
