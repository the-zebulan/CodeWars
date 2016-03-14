import unittest

from Kyu_7.filter_list import filter_list


class FilterListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])

    def test_equals_2(self):
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])

    def test_equals_3(self):
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]),
                         [1, 2, 123])


if __name__ == '__main__':
    unittest.main()
