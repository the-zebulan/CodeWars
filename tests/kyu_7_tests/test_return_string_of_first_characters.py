import unittest

from Kyu_7.return_string_of_first_characters import make_string


class MakeStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_string('sees eyes xray yoat'), 'sexy')

    def test_equals_2(self):
        self.assertEqual(make_string('brown eyes are nice'), 'bean')

    def test_equals_3(self):
        self.assertEqual(make_string('cars are very nice'), 'cavn')

    def test_equals_4(self):
        self.assertEqual(make_string('kaks de gan has a big head'), 'kdghabh')


if __name__ == '__main__':
    unittest.main()
