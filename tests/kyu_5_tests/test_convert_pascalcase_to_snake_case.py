import unittest

from katas.kyu_5.convert_pascalcase_to_snake_case import to_underscore


class PascalToSnakeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_underscore('TestController'), 'test_controller')

    def test_equals_2(self):
        self.assertEqual(to_underscore(5), '5')
