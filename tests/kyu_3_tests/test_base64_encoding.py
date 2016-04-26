import unittest

from katas.kyu_3.base64_encoding import to_base_64, from_base_64


class Base64TestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases = iter((
            ['this is a string!!', 'dGhpcyBpcyBhIHN0cmluZyEh'],
            ['this is a test!', 'dGhpcyBpcyBhIHRlc3Qh'],
            ['now is the time for all good men to come to the aid of their '
             'country.',
             'bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0a'
             'GUgYWlkIG9mIHRoZWlyIGNvdW50cnku'],
            ['1234567890  ', 'MTIzNDU2Nzg5MCAg'],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ ',
             'QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog'],
            ['the quick brown fox jumps over the white fence. ',
             'dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5j'
             'ZS4g'],
            ['dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZ'
             'S4',
             'ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU'
             '0IzYUdsMFpTQm1aVzVqWlM0'],
            ['VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna',
             'VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h'],
            ['TVRJek5EVTJOemc1TUNBZyAg', 'VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn']
        ))

    def test_equal_1(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_2(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_3(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_4(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_5(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_6(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_7(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_8(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)

    def test_equal_9(self):
        left, right = next(self.test_cases)
        self.assertEqual(to_base_64(left), right)
        self.assertEqual(from_base_64(right), left)


if __name__ == '__main__':
    unittest.main()
