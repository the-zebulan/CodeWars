import unittest

from kyu_6.patterncraft_strategy import Fly, Viking


class VikingTestCase(unittest.TestCase):
    def test_equals(self):
        viking = Viking()
        viking.move()
        self.assertEqual(viking.position, 1)
        viking.move()
        self.assertEqual(viking.position, 2)

    def test_equals_2(self):
        viking = Viking()
        viking.move_behavior = Fly()
        viking.move()
        self.assertEqual(viking.position, 10)
        viking.move()
        self.assertEqual(viking.position, 20)

    def test_equals_3(self):
        viking = Viking()
        viking.move()
        self.assertEqual(viking.position, 1)
        viking.move_behavior = Fly()
        viking.move()
        self.assertEqual(viking.position, 11)


if __name__ == '__main__':
    unittest.main()
