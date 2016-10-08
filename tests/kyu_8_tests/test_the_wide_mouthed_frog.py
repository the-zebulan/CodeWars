import unittest

from katas.kyu_8.the_wide_mouthed_frog import mouth_size


class MouthSizeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(mouth_size('toucan'), 'wide')

    def test_equal_2(self):
        self.assertEqual(mouth_size('ant bear'), 'wide')

    def test_equal_3(self):
        self.assertEqual(mouth_size('alligator'), 'small')
