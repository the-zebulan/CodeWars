import unittest

from katas.kyu_7.author_disambiguation_to_the_point import could_be


class CouldBeTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos Ray Norris'))

    def test_false_1(self):
        self.assertFalse(could_be('Carlos Ray Norris', 'Carlos Ray Norr'))

    def test_false_2(self):
        self.assertFalse(could_be('Steven Seagal', ' '))

    def test_false_3(self):
        self.assertFalse(could_be('', ''))
