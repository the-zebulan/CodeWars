import unittest

from katas.beta.which_string_is_worth_more import highest_value


class HighestValueTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(highest_value('AaBbCcXxYyZz0189', 'KkLlMmNnOoPp4567'),
                         'KkLlMmNnOoPp4567')

    def test_equal_2(self):
        self.assertEqual(highest_value('HELLO', 'GOODBYE'), 'GOODBYE')
