import unittest

import Beta.thinking_and_testing_03


class ThinkingAndTestingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(0), 0)

    def test_equals_2(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(2), 1)

    def test_equals_3(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(3), 2)

    def test_equals_4(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(4), 1)

    def test_equals_5(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(5), 2)

    def test_equals_6(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(6), 2)

    def test_equals_7(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(7), 3)

    def test_equals_8(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(8), 1)

    def test_equals_9(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(9), 2)

    def test_equals_10(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(10), 2)

    def test_equals_11(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(100), 3)

    def test_equals_12(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(1000), 6)

    def test_equals_13(self):
        self.assertEqual(Beta.thinking_and_testing_03.testit(10000), 5)


if __name__ == '__main__':
    unittest.main()
