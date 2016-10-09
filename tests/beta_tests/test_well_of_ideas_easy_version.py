import unittest

from katas.kyu_8.well_of_ideas_easy_version import well


class WellOfIdeasTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(well(['bad', 'bad', 'bad']), 'Fail!')

    def test_equal_2(self):
        self.assertEqual(well(
            ['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')

    def test_equal_3(self):
        self.assertEqual(well([
            'good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']),
            'I smell a series!')
