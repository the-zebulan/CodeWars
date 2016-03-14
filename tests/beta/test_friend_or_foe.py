import unittest

from Beta.friend_or_foe import friend


class FriendTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(friend(['Ryan', 'Kieran', 'Mark']), ['Ryan', 'Mark'])


if __name__ == '__main__':
    unittest.main()
