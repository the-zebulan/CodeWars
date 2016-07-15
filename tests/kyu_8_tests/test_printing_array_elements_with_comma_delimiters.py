import unittest

from katas.kyu_8.printing_array_elements_with_comma_delimiters import \
    print_array


class PrintCommaDelimitedTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(print_array([2]), '2')

    def test_equal_2(self):
        self.assertEqual(print_array([2, 4, 5, 2]), '2,4,5,2')

    def test_equal_3(self):
        self.assertEqual(print_array([2, 4, 5, 2]), '2,4,5,2')

    def test_equal_4(self):
        self.assertEqual(print_array([2.0, 4.2, 5.1, 2.2]), '2.0,4.2,5.1,2.2')

    def test_equal_5(self):
        self.assertEqual(print_array(['2', '4', '5', '2']), '2,4,5,2')

    def test_equal_6(self):
        self.assertEqual(print_array([True, False, False]), 'True,False,False')

    def test_equal_7(self):
        self.assertEqual(print_array(
            ['hello', 'this', 'is', 'an', 'array!'] +
            ['a', 'b', 'c', 'd', 'e!']
        ), 'hello,this,is,an,array!,a,b,c,d,e!')

    def test_equal_8(self):
        self.assertEqual(print_array([
            ['hello', 'this', 'is', 'an', 'array!'], [1, 2, 3, 4, 5]
        ]), "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]")
