import unittest

from Kyu_6.which_are_in import in_array


class InArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(in_array(
            ['live', 'arp', 'strong'],
            ['lively', 'alive', 'harp', 'sharp', 'armstrong']),
            ['arp', 'live', 'strong'])


if __name__ == '__main__':
    unittest.main()
