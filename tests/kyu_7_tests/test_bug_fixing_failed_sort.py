import unittest

from kyu_7.bug_fixing_failed_sort import sort_array


class SortArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sort_array('12345'), '12345')

    def test_equals_2(self):
        self.assertEqual(sort_array('54321'), '12345')

    def test_equals_3(self):
        self.assertEqual(sort_array('34251'), '12345')


if __name__ == '__main__':
    unittest.main()
