import unittest

from katas.kyu_7.ordering_the_words import order_word


class OrderingTheWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(order_word('Hello, World!'), ' !,HWdellloor')

    def test_equals_2(self):
        self.assertEqual(order_word('bobby'), 'bbboy')

    def test_equals_3(self):
        self.assertEqual(order_word(''), 'Invalid String!')

    def test_equals_4(self):
        self.assertEqual(order_word('completesolution'), 'ceeillmnooopsttu')

    def test_equals_5(self):
        self.assertEqual(order_word('\"][@!#$*(^&%'), '!\"#$%&(*@[]^')

    def test_equals_6(self):
        self.assertEqual(
            order_word('i\"d][@z!#$r(^a&world%'), '!\"#$%&(@[]^addilorrwz'
        )

    def test_equals_7(self):
        self.assertEqual(order_word(None), 'Invalid String!')


if __name__ == '__main__':
    unittest.main()
