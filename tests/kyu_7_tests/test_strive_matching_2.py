import unittest

from katas.kyu_7.strive_matching_2 import match


class StriveMatchingTestCase(unittest.TestCase):
    def setUp(self):
        self.candidates = [{
            'desires_equity': True,
            'current_location': 'New York',
            'desired_locations': ['San Francisco', 'Los Angeles']
            }, {
            'desires_equity': False,
            'current_location': 'San Francisco',
            'desired_locations': ['Kentucky', 'New Mexico']
        }]

    def test_equals(self):
        self.assertEqual(len(match({
            'equity_max': 0, 'locations': ['Los Angeles', 'New York']},
            self.candidates)), 0)

    def test_equals_2(self):
        self.assertEqual(len(match({
            'equity_max': 1.2, 'locations': ['New York', 'Kentucky']},
            self.candidates)), 2)


if __name__ == '__main__':
    unittest.main()
