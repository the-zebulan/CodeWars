import unittest

from kyu_7.supernatural import bob


class BobTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bob('vampire'), 'Behead it with a machete, idjits!')

    def test_equals_2(self):
        self.assertEqual(bob('pagan god'),
                         'It depends on which one it is, idjits!')

    def test_equals_3(self):
        self.assertEqual(bob('werepuppy'),
                         'I have friggin no idea yet, idjits!')


if __name__ == '__main__':
    unittest.main()
