import unittest

from Kyu_8.bug_fixing_11 import validate


class ValidateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(validate('Timmy', 'password'),
                         'Successfully Logged in!')

    def test_equals_2(self):
        self.assertEqual(validate('Timmy', 'h4x0r'),
                         'Wrong username or password!')

    def test_equals_3(self):
        self.assertEqual(validate('Alice', 'alice'),
                         'Successfully Logged in!')

    def test_equals_4(self):
        self.assertEqual(validate('Timmy', 'password"||""=="'),
                         'Wrong username or password!')

    def test_equals_5(self):
        self.assertEqual(validate('Admin', 'gs5bw"||1==1//'),
                         'Wrong username or password!')


if __name__ == '__main__':
    unittest.main()
