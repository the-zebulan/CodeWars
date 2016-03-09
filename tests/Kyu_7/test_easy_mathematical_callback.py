import unittest

from Kyu_7.easy_mathematical_callback import process_array


class ProcessArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(
            process_array([4, 8, 2, 7, 5], lambda val: val * 2),
            [8, 16, 4, 14, 10]
        )

    def test_equals_2(self):
        self.assertEqual(
            process_array([7, 8, 9, 1, 2], lambda val: val + 5),
            [12, 13, 14, 6, 7]
        )

    def test_equals_3(self):
        self.assertEqual(
            process_array([-1, 1, 2, 3, 4, 5], lambda val: val ** 3),
            [-1, 1, 8, 27, 64, 125]
        )

    def test_equals_4(self):
        self.assertEqual(process_array([], lambda val: val + 1), [])


if __name__ == '__main__':
    unittest.main()
