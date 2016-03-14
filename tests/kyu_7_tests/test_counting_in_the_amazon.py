import unittest

from kyu_7.counting_in_the_amazon import count_arara


class CountAraraTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_arara(1), 'anane')

    def test_equals_2(self):
        self.assertEqual(count_arara(2), 'adak')

    def test_equals_3(self):
        self.assertEqual(count_arara(3), 'adak anane')

    def test_equals_4(self):
        self.assertEqual(count_arara(9), 'adak adak adak adak anane')


if __name__ == '__main__':
    unittest.main()
