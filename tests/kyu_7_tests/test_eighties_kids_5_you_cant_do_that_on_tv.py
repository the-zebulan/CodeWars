import unittest

from katas.kyu_7.eighties_kids_5_you_cant_do_that_on_tv import bucket_of


class BucketTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bucket_of('wet water'), 'water')

    def test_equals_2(self):
        self.assertEqual(bucket_of('slime water'), 'sludge')

    def test_equals_3(self):
        self.assertEqual(bucket_of(
            'I don\'t know if this will work'), 'slime')

    def test_equals_4(self):
        self.assertEqual(bucket_of(
            'I don\'t know if this will work without watering it first.'),
            'sludge')

    def test_equals_5(self):
        self.assertEqual(bucket_of(''), 'air')

    def test_equals_6(self):
        self.assertEqual(bucket_of('slimeslimeslimeslimewater'), 'sludge')


if __name__ == '__main__':
    unittest.main()
