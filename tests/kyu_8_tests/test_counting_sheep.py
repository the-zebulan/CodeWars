import unittest

from katas.kyu_8.counting_sheep import count_sheeps


class CountSheepTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_sheeps([
            True, True, True, False, True, True, True, True, True, False,
            True, False, True, False, False, True, True, True, True, True,
            False, False, True, True
        ]), 17)
