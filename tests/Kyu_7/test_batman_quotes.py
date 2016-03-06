import unittest

from Kyu_7.batman_quotes import BatmanQuotes


class BatmanQuotesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(BatmanQuotes.get_quote([
            'WHERE IS SHE?!', 'Holy haberdashery, Batman!',
            'Let\'s put a smile on that faaaceee!'], 'Rob1n'
        ), 'Robin: Holy haberdashery, Batman!')


if __name__ == '__main__':
    unittest.main()
