import unittest

from katas.kyu_6.which_are_in import in_array


class InArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(in_array(
            ['live', 'arp', 'strong'],
            ['lively', 'alive', 'harp', 'sharp', 'armstrong']),
            ['arp', 'live', 'strong'])
