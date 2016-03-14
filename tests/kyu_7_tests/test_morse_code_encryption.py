import unittest

from Kyu_7.morse_code_encryption import encryption


class EncryptionTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(encryption('HELLO WORLD'),
                         '.... . .-.. .-.. ---   .-- --- .-. .-.. -..')

    def test_equals_2(self):
        self.assertEqual(encryption('SOS'), '... --- ...')

    def test_equals_3(self):
        self.assertEqual(encryption('1836'), '.---- ---.. ...-- -....')

    def test_equals_4(self):
        self.assertEqual(encryption('THE QUICK BROWN FOX'),
                         '- .... .   --.- ..- .. -.-. -.-   -... .-. --- .--'
                         ' -.   ..-. --- -..-')

    def test_equals_5(self):
        self.assertEqual(encryption('JUMPED OVER THE'),
                         '.--- ..- -- .--. . -..   --- ...- . .-.   - .... .')


if __name__ == '__main__':
    unittest.main()
