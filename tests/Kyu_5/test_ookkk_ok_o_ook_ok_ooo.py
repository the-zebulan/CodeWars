import unittest

from Kyu_5.ookkk_ok_o_ook_ok_ooo import okkOokOo


class OKTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(okkOokOo('Ok, Ook, Ooo!'), 'H')

    def test_equals_2(self):
        self.assertEqual(okkOokOo('Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?  Okk, Okkkk!'), 'Hello')

    def test_equals_3(self):
        self.assertEqual(okkOokOo('Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Okk, Oo?  Okk, Ook, Oo?  Ook, Ooook!'), 'World!')


if __name__ == '__main__':
    unittest.main()
