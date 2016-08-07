import unittest

from katas.beta.get_number_from_string import get_number_from_string


class GetNumberFromStringTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_number_from_string('1'), 1)

    def test_equal_2(self):
        self.assertEqual(get_number_from_string('123'), 123)

    def test_equal_3(self):
        self.assertEqual(get_number_from_string('this is number: 7'), 7)

    def test_equal_4(self):
        self.assertEqual(get_number_from_string('$100 000 000'), 100000000)

    def test_equal_5(self):
        self.assertEqual(get_number_from_string('hell5o wor6ld'), 56)

    def test_equal_6(self):
        self.assertEqual(
            get_number_from_string('one1 two2 three3 four4 five5'), 12345
        )
