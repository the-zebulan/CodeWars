import unittest

from katas.beta.pirates_are_the_cannons_ready import cannons_ready


class CannonsReadyTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cannons_ready({
            'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'
        }), 'Fire!')

    def test_equal_2(self):
        self.assertEqual(cannons_ready({
            'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'
        }), 'Shiver me timbers!')
