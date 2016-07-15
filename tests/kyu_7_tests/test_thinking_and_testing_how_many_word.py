import unittest

from katas.kyu_7.thinking_and_testing_how_many_word import testit as solution


class HowManyWordTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution('word'), 1)

    def test_equals_2(self):
        self.assertEqual(solution('hello world'), 1)

    def test_equals_3(self):
        self.assertEqual(solution('I love codewars.'), 0)

    def test_equals_4(self):
        self.assertEqual(solution('My cat waiting for a dog.'), 1)

    def test_equals_5(self):
        self.assertEqual(
            solution('We often read book, a word hidden in the book.'), 2
        )

    def test_equals_6(self):
        self.assertEqual(
            solution('When you in order to do something by a wrong way, your'
                     ' heart will missed somewhere.'), 2
        )

    def test_equals_7(self):
        self.assertEqual(solution('This sentence has one word.'), 1)

    def test_equals_8(self):
        self.assertEqual(
            solution('This sentence has two words, not one word.'), 2
        )

    def test_equals_9(self):
        self.assertEqual(
            solution('One word + one word = three words -)'), 3
        )

    def test_equals_10(self):
        self.assertEqual(solution('Can you find more word for me?'), 1)
