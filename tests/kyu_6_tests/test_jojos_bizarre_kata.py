import unittest

from katas.kyu_6.jojos_bizarre_kata import is_jojo


class JoJoTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_jojo('Jonathan Joestar'))

    def test_false(self):
        self.assertFalse(is_jojo('Dio Brando'))


if __name__ == '__main__':
    unittest.main()
