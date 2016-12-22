import unittest

from katas.beta.how_many_times_does_it_contain import string_counter


class StringCounterTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(string_counter('Hello world', 'o'), 2)

    def test_equal_2(self):
        self.assertEqual(string_counter(
            "Wait isn't it supposed to be cynical?", 'i'), 4)

    def test_equal_3(self):
        self.assertEqual(string_counter(
            "I'm gona be the best code warrior ever dad", 'r'), 4)

    def test_equal_4(self):
        self.assertEqual(string_counter('Do you like Harry Potter?', '?'), 1)
