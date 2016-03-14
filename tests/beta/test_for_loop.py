import unittest

from Beta.for_loop import problem


class ProblemTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(problem(5), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
