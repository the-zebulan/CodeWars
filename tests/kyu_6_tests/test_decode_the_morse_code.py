import unittest

from katas.kyu_6.decode_the_morse_code import decodeMorse


class DecodeMorseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'),
                         'HEY JUDE')

    def test_equals_2(self):
        self.assertEqual(decodeMorse('... --- ...'), 'SOS')

    def test_equals_3(self):
        self.assertEqual(decodeMorse(
            '...---... -.-.-- - .... . --.- ..- .. -.-. -.- -... .-. --- .--'
            ' -. ..-. --- -..- .--- ..- -- .--. ... --- ...- . .-. - .... . '
            '.-.. .- --.. -.-- -.. --- --. .-.-.-'),
            'SOS!THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG.')


if __name__ == '__main__':
    unittest.main()
