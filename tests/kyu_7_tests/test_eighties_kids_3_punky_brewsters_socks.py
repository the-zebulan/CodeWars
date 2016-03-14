import unittest

from Kyu_7.eighties_kids_3_punky_brewsters_socks import get_socks


class GetSocksTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_socks(
            'Punky', ['pink', 'argyle', 'argyle']), ['pink', 'argyle'])

    def test_equals_2(self):
        self.assertEqual(get_socks(
            'Henry', ['red', 'blue', 'blue', 'green']), ['blue', 'blue'])

    def test_equals_3(self):
        self.assertEqual(get_socks(
            'Punky', ['pink', 'pink', 'pink', 'pink']), [])

    def test_equals_4(self):
        self.assertEqual(get_socks(
            'Punky', ['blue', 'blue', 'blue', 'green', 'green']
        ), ['blue', 'green'])

    def test_equals_5(self):
        self.assertEqual(get_socks(
            'Henry', ['green', 'blue', 'pink', 'argyle']), [])

    def test_equals_6(self):
        self.assertEqual(get_socks(
            'Henry', ['argyle', 'green', 'dirty sock', 'argyle']
        ), ['argyle', 'argyle'])

    def test_equals_7(self):
        self.assertEqual(get_socks('Henry', ['green']), [])

    def test_equals_8(self):
        self.assertEqual(get_socks('Punky', ['green']), [])

    def test_equals_9(self):
        self.assertEqual(get_socks('Henry', []), [])

    def test_equals_10(self):
        self.assertEqual(get_socks('Punky', []), [])


if __name__ == '__main__':
    unittest.main()
