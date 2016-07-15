import unittest

from katas.beta.find_something_in_an_array import find


class FindTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(find('hello', ['bye bye', 'hello']))

    def test_false(self):
        self.assertFalse(find('anything', ['bye bye', 'hello']))
