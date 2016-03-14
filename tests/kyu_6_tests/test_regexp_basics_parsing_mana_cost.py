import unittest

from katas.kyu_6.regexp_basics_parsing_mana_cost import parse_mana_cost


class ParseManaCostTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(parse_mana_cost(''), {})

    def test_equals_2(self):
        self.assertEqual(parse_mana_cost('0'), {})

    def test_equals_3(self):
        self.assertEqual(parse_mana_cost('1'), {'*': 1})

    def test_equals_4(self):
        self.assertEqual(parse_mana_cost('4'), {'*': 4})

    def test_equals_5(self):
        self.assertEqual(parse_mana_cost('15'), {'*': 15})

    def test_equals_6(self):
        self.assertEqual(parse_mana_cost('2rr'), {'*': 2, 'r': 2})

    def test_equals_7(self):
        self.assertEqual(parse_mana_cost('1wbg'),
                         {'*': 1, 'w': 1, 'b': 1, 'g': 1})

    def test_equals_8(self):
        self.assertEqual(parse_mana_cost('1WWU'), {'*': 1, 'w': 2, 'u': 1})

    def test_equals_9(self):
        self.assertEqual(parse_mana_cost('0r'), {'r': 1})

    def test_equals_10(self):
        self.assertEqual(parse_mana_cost('2R'), {'*': 2, 'r': 1})

    def test_equals_11(self):
        self.assertEqual(parse_mana_cost('b'), {'b': 1})

    def test_none(self):
        self.assertIsNone(parse_mana_cost('2x'))

    def test_none_2(self):
        self.assertIsNone(parse_mana_cost('2\n'))

    def test_none_3(self):
        self.assertIsNone(parse_mana_cost('\n2'))


if __name__ == '__main__':
    unittest.main()
