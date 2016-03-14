import unittest

from kyu_6.hamming_distance import hamming


class HammingDistanceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(hamming('I like turtles', 'I like turkeys'), 3)

    def test_equals_2(self):
        self.assertEqual(hamming('Hello World', 'Hello World'), 0)


if __name__ == '__main__':
    unittest.main()
