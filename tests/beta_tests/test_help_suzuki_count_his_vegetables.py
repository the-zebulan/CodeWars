import unittest

from katas.beta.help_suzuki_count_his_vegetables import count_vegetables


class CountVegetablesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_vegetables(
            'potato tofu cucumber cabbage turnip pepper onions carrots celery'
            ' mushrooms potato tofu cucumber cabbage'),
            [(2, 'tofu'), (2, 'potato'), (2, 'cucumber'), (2, 'cabbage'),
             (1, 'turnip'), (1, 'pepper'), (1, 'onions'), (1, 'mushrooms'),
             (1, 'celery'), (1, 'carrots')]
        )

    def test_equals_2(self):
        self.assertEqual(count_vegetables(
            'mushrooms chopsticks chopsticks turnip mushrooms carrots mushroo'
            'ms cabbage mushrooms carrots tofu pepper cabbage potato cucumber'
            ' mushrooms mushrooms mushrooms potato turnip chopsticks cabbage '
            'celery celery turnip pepper chopsticks potato potato onions cabb'
            'age cucumber onions pepper onions cabbage potato tofu carrots ca'
            'bbage cabbage turnip mushrooms cabbage cabbage cucumber cabbage '
            'chopsticks turnip pepper onions pepper onions mushrooms turnip c'
            'arrots carrots tofu onions tofu chopsticks chopsticks chopsticks'
            ' mushrooms cucumber chopsticks carrots potato cabbage cabbage ca'
            'rrots mushrooms chopsticks mushrooms celery turnip onions carrot'
            's turnip cucumber carrots potato mushrooms turnip mushrooms cabb'
            'age tofu turnip turnip turnip mushrooms tofu potato pepper turni'
            'p potato turnip celery carrots turnip'),
            [(15, 'turnip'), (15, 'mushrooms'), (13, 'cabbage'),
             (10, 'carrots'), (9, 'potato'), (7, 'onions'), (6, 'tofu'),
             (6, 'pepper'), (5, 'cucumber'), (4, 'celery')]
        )


if __name__ == '__main__':
    unittest.main()
