import unittest

from Beta.beginner_series_cockroach import cockroach_speed


class CockroachSpeedTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(cockroach_speed(1.08), 30)

    def test_equals_2(self):
        self.assertEqual(cockroach_speed(1.09), 30)

    def test_equals_3(self):
        self.assertEqual(cockroach_speed(0), 0)


if __name__ == '__main__':
    unittest.main()
