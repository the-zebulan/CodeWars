import unittest

from katas.beta.string_to_list_of_integers import string_to_int_list


class StringToIntegerListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(string_to_int_list('1,2,3,4,5'), [1, 2, 3, 4, 5])

    def test_equal_2(self):
        self.assertEqual(string_to_int_list('21,12,23,34,45'),
                         [21, 12, 23, 34, 45])

    def test_equal_3(self):
        self.assertEqual(string_to_int_list('-1,-2,3,-4,-5'),
                         [-1, -2, 3, -4, -5])

    def test_equal_4(self):
        self.assertEqual(string_to_int_list('1,2,3,,,4,,5,,,'),
                         [1, 2, 3, 4, 5])

    def test_equal_5(self):
        self.assertEqual(string_to_int_list(',,,,,1,2,3,,,4,,5,,,'),
                         [1, 2, 3, 4, 5])

    def test_equal_6(self):
        self.assertEqual(string_to_int_list(''), [])

    def test_equal_7(self):
        self.assertEqual(string_to_int_list(',,,,,,,,'), [])


if __name__ == '__main__':
    unittest.main()
