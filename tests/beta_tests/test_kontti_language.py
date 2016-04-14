import unittest

from katas.beta.kontti_language import kontti


class KonttiTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(kontti('lamppu'), 'komppu-lantti')

    def test_equals_2(self):
        self.assertEqual(kontti('lamppu sofia'), 'komppu-lantti kofia-sontti')

    def test_equals_3(self):
        self.assertEqual(kontti('silly game'), 'kolly-sintti kome-gantti')

    def test_equals_4(self):
        self.assertEqual(kontti('aeiou'), 'koeiou-antti')

    def test_equals_5(self):
        self.assertEqual(kontti('xyz lamppu'), 'xyz komppu-lantti')

    def test_equals_6(self):
        self.assertEqual(kontti(''), '')

    def test_equals_7(self):
        self.assertEqual(kontti('lAmppU'), 'komppU-lAntti')

    def test_equals_8(self):
        self.assertEqual(kontti('silly grrr'), 'kolly-sintti grrr')


if __name__ == '__main__':
    unittest.main()
