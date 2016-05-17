import unittest

from katas.beta.jacobs_weight_loss_program import lose_weight


class LoseWeightTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(lose_weight('K', 200, 10), 'Invalid gender')

    def test_equal_2(self):
        self.assertEqual(lose_weight('M', 0, 10), 'Invalid weight')

    def test_equal_3(self):
        self.assertEqual(lose_weight('F', 160, -10), 'Invalid duration')

    def test_equal_4(self):
        self.assertEqual(lose_weight('M', 250, 5), 231.8)

    def test_equal_5(self):
        self.assertEqual(lose_weight('F', 190, 8), 172.5)


if __name__ == '__main__':
    unittest.main()
