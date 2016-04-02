import unittest

from katas.kyu_8.count_the_monkeys import monkey_count


class MonkeyCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(monkey_count(5), [1, 2, 3, 4, 5])

    def test_equals_2(self):
        self.assertEqual(monkey_count(3), [1, 2, 3])

    def test_equals_3(self):
        self.assertEqual(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_equals_4(self):
        self.assertEqual(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_equals_5(self):
        self.assertEqual(
            monkey_count(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                               14, 15, 16, 17, 18, 19, 20]
        )


if __name__ == '__main__':
    unittest.main()
