import unittest

from katas.beta.upper_body_strength import alex_mistakes


class AlexMistakesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(alex_mistakes(10, 120), 3)

    def test_equal_2(self):
        self.assertEqual(alex_mistakes(11, 120), 3)

    def test_equal_3(self):
        self.assertEqual(alex_mistakes(3, 45), 2)

    def test_equal_4(self):
        self.assertEqual(alex_mistakes(8, 120), 3)

    def test_equal_5(self):
        self.assertEqual(alex_mistakes(6, 60), 2)

    def test_equal_6(self):
        self.assertEqual(alex_mistakes(9, 180), 4)

    def test_equal_7(self):
        self.assertEqual(alex_mistakes(20, 120), 0)

    def test_equal_8(self):
        self.assertEqual(alex_mistakes(20, 125), 1)

    def test_equal_9(self):
        self.assertEqual(alex_mistakes(20, 130), 1)

    def test_equal_10(self):
        self.assertEqual(alex_mistakes(20, 135), 2)


if __name__ == '__main__':
    unittest.main()
