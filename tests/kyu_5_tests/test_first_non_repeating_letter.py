import unittest

from katas.kyu_5.first_non_repeating_letter import first_non_repeating_letter


class FirstNonRepeatingLetterTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(first_non_repeating_letter('a'), 'a')

    def test_equal_2(self):
        self.assertEqual(first_non_repeating_letter('stress'), 't')

    def test_equal_3(self):
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')

    def test_equal_4(self):
        self.assertEqual(first_non_repeating_letter(''), '')

    def test_equal_5(self):
        self.assertEqual(first_non_repeating_letter('abba'), '')

    def test_equal_6(self):
        self.assertEqual(first_non_repeating_letter('aa'), '')

    def test_equal_7(self):
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')

    def test_equal_8(self):
        self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')

    def test_equal_9(self):
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')

    def test_equal_10(self):
        self.assertEqual(first_non_repeating_letter(
            "Go hang a salami, I'm a lasagna hog!"), ',')
