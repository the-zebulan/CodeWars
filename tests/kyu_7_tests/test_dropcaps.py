import unittest

from katas.kyu_7.dropcaps import drop_cap


class DropCapTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(drop_cap('more  than    one space between words'),
                         'More  Than    One Space Between Words')

    def test_equals_2(self):
        self.assertEqual(drop_cap('aRQh yBdbvhcRglvirAcRpXat NlahSCaPlMkol'),
                         'Arqh Ybdbvhcrglviracrpxat Nlahscaplmkol')


if __name__ == '__main__':
    unittest.main()
