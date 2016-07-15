import unittest

from katas.kyu_6.string_searching_with_wildcard import find


class FindTestCase(unittest.TestCase):
    def setUp(self):
        self.test = \
            'Once upon a midnight dreary, while I pondered, weak and weary'

    def test_equals(self):
        self.assertEqual(find('Once', self.test), 0)

    def test_equals_2(self):
        self.assertEqual(find('midnight', self.test), 12)

    def test_equals_3(self):
        self.assertEqual(find('codewars', self.test), -1)

    def test_equals_4(self):
        self.assertEqual(find('_po_', self.test), 5)

    def test_equals_5(self):
        self.assertEqual(find('___night', self.test), 12)

    def test_equals_6(self):
        self.assertEqual(find(
            '_lexe', 'googgoogleggggoooglxeplexhexflexmexkex'), -1)

    def test_equals_7(self):
        self.assertEqual(find('--_.,', '-..,.44$&%$--,.,'), 11)

    def test_equals_8(self):
        self.assertEqual(find('-..,.44$&%$--,.,', '-..,.44$&%$--,.,'), 0)

    def test_equals_9(self):
        self.assertEqual(find('___4$&%$--___', '-..,.44$&%$--,.,'), 3)
