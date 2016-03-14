import unittest

from katas.kyu_8.finish_guess_the_number_game import Guesser


class GuesserTestCase(unittest.TestCase):
    def test_true(self):
        guesser = Guesser(10, 2)
        guesser.guess(10)
        guesser.guess(10)
        guesser.guess(10)
        guesser.guess(10)
        self.assertTrue(guesser.guess(10))

    def test_false(self):
        guesser = Guesser(10, 2)
        guesser.guess(1)
        self.assertFalse(guesser.guess(1))


if __name__ == '__main__':
    unittest.main()
