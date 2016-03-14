import unittest

from Kyu_6.delete_nth_occurrence import delete_nth


class DeleteNthOccurrenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])

    def test_equals_2(self):
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
                         [1, 1, 3, 3, 7, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
