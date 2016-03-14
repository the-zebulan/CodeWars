import unittest

from kyu_8.lario_and_muigi_pipe_problem import pipe_fix


class PipeFixTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pipe_fix([1, 2, 3, 5, 6, 8, 9]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_equals_2(self):
        self.assertEqual(pipe_fix([1, 2, 3, 12]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_equals_3(self):
        self.assertEqual(pipe_fix([6, 9]), [6, 7, 8, 9])

    def test_equals_4(self):
        self.assertEqual(pipe_fix([-1, 4]), [-1, 0, 1, 2, 3, 4])

    def test_equals_5(self):
        self.assertEqual(pipe_fix([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
