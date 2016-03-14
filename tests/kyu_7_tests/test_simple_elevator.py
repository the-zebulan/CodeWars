import unittest

from kyu_7.simple_elevator import goto


class SimpleElevatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(goto(2, '4'), 0)

    def test_equals_2(self):
        self.assertEqual(goto(4, '0'), 0)

    def test_equals_3(self):
        self.assertEqual(goto(3, None), 0)

    def test_equals_4(self):
        self.assertEqual(goto(None, '2'), 0)

    def test_equals_5(self):
        self.assertEqual(goto([], '2'), 0)

    def test_equals_6(self):
        self.assertEqual(goto(3, {}), 0)

    def test_equals_7(self):
        self.assertEqual(goto(2, ''), 0)

    def test_equals_8(self):
        self.assertEqual(goto(0, '2'), 2)

    def test_equals_9(self):
        self.assertEqual(goto(3, '1'), -2)

    def test_equals_10(self):
        self.assertEqual(goto(2, '2'), 0)


if __name__ == '__main__':
    unittest.main()
