import unittest

from katas.beta.super_duper_easy import problem


class ProblemTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(problem('hello'), 'Error')

    def test_equals_2(self):
        self.assertEqual(problem(1), 56)


if __name__ == '__main__':
    unittest.main()
