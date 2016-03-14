import unittest

from Kyu_8.hello_world import greet


class HelloWorldTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greet(), 'hello world')


if __name__ == '__main__':
    unittest.main()
