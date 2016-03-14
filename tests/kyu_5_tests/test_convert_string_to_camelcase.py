import unittest

from kyu_5.convert_string_to_camelcase import to_camel_case


class ToCamelCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_camel_case('the-stealth-warrior'),
                         'theStealthWarrior')

    def test_equals_2(self):
        self.assertEqual(to_camel_case('The_Stealth_Warrior'),
                         'TheStealthWarrior')

    def test_equals_3(self):
        self.assertEqual(to_camel_case('A-B-C'), 'ABC')

    def test_equals_4(self):
        self.assertEqual(to_camel_case(''), '')


if __name__ == '__main__':
    unittest.main()
