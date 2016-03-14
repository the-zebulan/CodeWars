import unittest

from katas.beta.finding_averages import average


class AverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(average(
            'Hello please let me break your program'), 'Incorrect')

    def test_equals_2(self):
        self.assertEqual(average([70, 70]), 70)

    def test_equals_3(self):
        self.assertEqual(average([40, 20, 5]), 21)


if __name__ == '__main__':
    unittest.main()
