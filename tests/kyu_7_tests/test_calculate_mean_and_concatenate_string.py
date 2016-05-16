import unittest

from katas.kyu_7.calculate_mean_and_concatenate_string import mean


class MeanTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mean([
            'u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g',
            '1', '2', 'w', '8', 'o', '2', '0']),
            [3.6, 'udiwstagwo']
        )

    def test_equals_2(self):
        self.assertEqual(mean([
            '0', 'c', '7', 'x', '6', '2', '3', '5', 'w', '7', '0', 'y', 'v',
            'u', 'h', 'i', 'n', 'u', '0', '0']),
            [3.0, 'cxwyvuhinu']
        )

    def test_equals_3(self):
        self.assertEqual(mean([
            '0', 'u', 'a', 'y', '0', 'a', '9', 'q', '3', 'v', 'g', '7', '6',
            '4', 'y', 'd', '8', '6', '0', 'd']),
            [4.3, 'uayaqvgydd']
        )

    def test_equals_4(self):
        self.assertEqual(mean([
            's', 'n', '9', 'l', '0', 'm', 'i', 'z', '9', '7', 'y', '4', 'z',
            '3', '3', 'k', '4', '1', '0', 'k']),
            [4.0, 'snlmizyzkk']
        )

    def test_equals_5(self):
        self.assertEqual(mean([
            '5', 'v', 'u', 'k', '8', '4', '9', 'b', '9', 'g', '5', 'z', '3',
            'f', '6', 'u', 'i', '6', '6', 't']),
            [6.1, 'vukbgzfuit']
        )


if __name__ == '__main__':
    unittest.main()
