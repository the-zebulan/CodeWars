import unittest

from katas.kyu_8.did_she_say_hello import validate_hello


class ValidateHelloTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_hello('hello'))

    def test_true_2(self):
        self.assertTrue(validate_hello('ciao bella!'))

    def test_true_3(self):
        self.assertTrue(validate_hello('salut'))

    def test_true_4(self):
        self.assertTrue(validate_hello('hallo, salut'))

    def test_true_5(self):
        self.assertTrue(validate_hello('hombre! Hola!'))

    def test_true_6(self):
        self.assertTrue(validate_hello('Hallo, wie geht\'s dir?'))

    def test_true_7(self):
        self.assertTrue(validate_hello('AHOJ!'))

    def test_true_8(self):
        self.assertTrue(validate_hello('czesc'))

    def test_true_9(self):
        self.assertTrue(validate_hello('Ahoj'))

    def test_false(self):
        self.assertFalse(validate_hello('meh'))
