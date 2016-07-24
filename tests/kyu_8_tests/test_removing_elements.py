import unittest

from katas.kyu_8.removing_elements import remove_every_other


class RemoveEveryOtherTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(remove_every_other([1]), [1])

    def test_equal_2(self):
        self.assertEqual(remove_every_other([[1, 2, 3, 4, 5]]),
                         [[1, 2, 3, 4, 5]])

    def test_equal_3(self):
        self.assertEqual(remove_every_other(['Hello', 'Goodbye']), ['Hello'])

    def test_equal_4(self):
        self.assertEqual(remove_every_other([1.013, 2398.00]), [1.013])

    def test_equal_5(self):
        self.assertEqual(
            remove_every_other(['Yes', 'No', 'Yes', 'No', 'Yes', 'No']),
            ['Yes', 'Yes', 'Yes']
        )

    def test_equal_6(self):
        self.assertEqual(remove_every_other(
            [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6, 7], [8, 9, 10, 11, 12]]
        ), [[1, 2], [3, 4], [5, 6, 7]])
