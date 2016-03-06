import unittest

from Kyu_8.return_to_sanity import mystery


class MysteryTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mystery(), {'sanity': 'Hello'})


if __name__ == '__main__':
    unittest.main()
