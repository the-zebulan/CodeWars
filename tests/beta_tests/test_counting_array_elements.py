import unittest

from katas.beta.counting_array_elements import count


class CountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count(['a', 'a', 'b', 'b', 'b']), {'a': 2, 'b': 3})
