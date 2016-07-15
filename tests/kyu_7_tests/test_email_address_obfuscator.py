import unittest

from katas.kyu_7.email_address_obfuscator import obfuscate


class ObfuscateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(obfuscate('test@123.com'), 'test [at] 123 [dot] com')

    def test_equals_2(self):
        self.assertEqual(obfuscate('Code_warrior@foo.ac.uk'),
                         'Code_warrior [at] foo [dot] ac [dot] uk')
