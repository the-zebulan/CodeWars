import unittest

from katas.kyu_6.decipher_this import decipher_this


class DecipherThisTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decipher_this('72olle 103doo 100ya'),
                         'Hello good day')

    def test_equal_2(self):
        self.assertEqual(decipher_this('82yade 115te 103o'), 'Ready set go')

    def test_equal_3(self):
        self.assertEqual(decipher_this(
            '65 119esi 111dl 111lw 108dvei 105n 97n 111ka'),
            'A wise old owl lived in an oak')

    def test_equal_4(self):
        self.assertEqual(decipher_this(
            '84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp'),
            'The more he saw the less he spoke')

    def test_equal_5(self):
        self.assertEqual(decipher_this(
            '84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare'),
            'The less he spoke the more he heard')

    def test_equal_6(self):
        self.assertEqual(decipher_this(
            '87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri'),
            'Why can we not all be like that wise old bird')

    def test_equal_7(self):
        self.assertEqual(decipher_this(
            '84kanh 121uo 80roti 102ro 97ll 121ruo 104ple'),
            'Thank you Piotr for all your help')
