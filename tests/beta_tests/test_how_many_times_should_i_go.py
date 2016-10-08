import unittest

from katas.beta.how_many_times_should_i_go import how_many_times


class HowManyTimesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(how_many_times(40, 15), 3)

    def test_equal_2(self):
        self.assertEqual(how_many_times(30, 10), 3)

    def test_equal_3(self):
        self.assertEqual(how_many_times(80, 15), 6)
