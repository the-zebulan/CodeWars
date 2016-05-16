import unittest

from katas.kyu_7.help_suzuki_count_his_vegetables import count_vegetables


class CountVegetablesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_vegetables(
            'potato tofu cucumber cabbage turnip pepper onion carrot celery'
            ' mushroom potato tofu cucumber cabbage'),
            [(2, 'tofu'), (2, 'potato'), (2, 'cucumber'), (2, 'cabbage'),
             (1, 'turnip'), (1, 'pepper'), (1, 'onion'), (1, 'mushroom'),
             (1, 'celery'), (1, 'carrot')]
        )

    def test_equals_2(self):
        self.assertEqual(count_vegetables(
            'mushroom chopsticks chopsticks turnip mushroom carrot mushroom '
            'cabbage mushroom carrot tofu pepper cabbage potato cucumber mus'
            'hroom mushroom mushroom potato turnip chopsticks cabbage celery'
            ' celery turnip pepper chopsticks potato potato onion cabbage cu'
            'cumber onion pepper onion cabbage potato tofu carrot cabbage ca'
            'bbage turnip mushroom cabbage cabbage cucumber cabbage chopstic'
            'ks turnip pepper onion pepper onion mushroom turnip carrot carr'
            'ot tofu onion tofu chopsticks chopsticks chopsticks mushroom cu'
            'cumber chopsticks carrot potato cabbage cabbage carrot mushroom'
            ' chopsticks mushroom celery turnip onion carrot turnip cucumber'
            ' carrot potato mushroom turnip mushroom cabbage tofu turnip tur'
            'nip turnip mushroom tofu potato pepper turnip potato turnip cel'
            'ery carrot turnip'),
            [(15, 'turnip'), (15, 'mushroom'), (13, 'cabbage'),
             (10, 'carrot'), (9, 'potato'), (7, 'onion'), (6, 'tofu'),
             (6, 'pepper'), (5, 'cucumber'), (4, 'celery')]
        )


if __name__ == '__main__':
    unittest.main()
