import unittest

from katas.beta.rigged_dice import throw_rigged


class MyTestCase(unittest.TestCase):
    @staticmethod
    def count_sixes():
        return sum(throw_rigged() == 6 for _ in xrange(100000))

    def test_true_1(self):
        self.assertTrue(any(
            21700 <= self.count_sixes() <= 22300 for _ in xrange(10)
        ))


if __name__ == '__main__':
    unittest.main()
