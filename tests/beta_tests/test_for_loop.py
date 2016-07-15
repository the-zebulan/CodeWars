import unittest

from katas.beta.for_loop import problem


class ProblemTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(problem(5), [1, 2, 3, 4, 5])
