import unittest

from katas.kyu_7.thinking_and_testing_something_capitalized import \
    testit as solution
# py.test seems to have issues when function name has 'test' in it


class SomethingCapitalizedTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(''), '')

    def test_equals_2(self):
        self.assertEqual(solution('a'), 'A')

    def test_equals_3(self):
        self.assertEqual(solution('b'), 'B')

    def test_equals_4(self):
        self.assertEqual(solution('a a'), 'A A')

    def test_equals_5(self):
        self.assertEqual(solution('a b'), 'A B')

    def test_equals_6(self):
        self.assertEqual(solution('a b c'), 'A B C')


if __name__ == '__main__':
    unittest.main()
