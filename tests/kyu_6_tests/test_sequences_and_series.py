import unittest

from katas.kyu_6.sequences_and_series import get_score


class GetScoreTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_score(1), 50)

    def test_equals_2(self):
        self.assertEqual(get_score(2), 150)

    def test_equals_3(self):
        self.assertEqual(get_score(3), 300)

    def test_equals_4(self):
        self.assertEqual(get_score(4), 500)

    def test_equals_5(self):
        self.assertEqual(get_score(5), 750)
