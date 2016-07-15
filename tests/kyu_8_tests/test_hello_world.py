import unittest

from katas.kyu_8.hello_world import greet


class HelloWorldTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greet(), 'hello world')
