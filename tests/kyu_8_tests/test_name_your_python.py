import unittest

from katas.kyu_8.name_your_python import Python


class NameYourPythonTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Python('Guido').name, 'Guido')


if __name__ == '__main__':
    unittest.main()
