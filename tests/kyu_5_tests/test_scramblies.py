import unittest

from katas.kyu_5.scramblies import scramble


class ScrambliesTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(scramble('rkqodlw', 'world'))

    def test_true_2(self):
        self.assertTrue(scramble('cedewaraaossoqqyt', 'codewars'))

    def test_true_3(self):
        self.assertTrue(scramble('scriptjava', 'javascript'))

    def test_true_4(self):
        self.assertTrue(scramble('scriptingjava', 'javascript'))

    def test_false(self):
        self.assertFalse(scramble('katas', 'steak'))


if __name__ == '__main__':
    unittest.main()
