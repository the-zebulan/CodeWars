import unittest

from Kyu_8.grasshopper_bug_squashing import (
    coins, health, log, main, position
)


class GrasshopperTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(coins, 0)

    def test_equals_2(self):
        self.assertEqual(health, 100)

    def test_equals_3(self):
        self.assertEqual(position, 0)

    def test_equals_4(self):
        self.assertEqual(log, ['roll_dice', 'move', 'combat', 'get_coins',
                               'buy_health', 'print_status'])

    def test_equals_5(self):
        self.assertIsNone(main())


if __name__ == '__main__':
    unittest.main()
