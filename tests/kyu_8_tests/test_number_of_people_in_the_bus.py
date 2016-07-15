import unittest

from katas.kyu_8.number_of_people_in_the_bus import number


class PeopleInTheBusTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(number([[10, 0], [3, 5], [5, 8]]), 5)

    def test_equals_2(self):
        self.assertEqual(number(
            [[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)

    def test_equals_3(self):
        self.assertEqual(number(
            [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)
