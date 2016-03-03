import unittest

from Beta.new_gps_system import check_distance, total_kilometers


class NewGPSSystemTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(total_kilometers(9.3, 87.3), 938.71)

    def test_equals_2(self):
        self.assertEqual(total_kilometers(11.7, 63.4), 541.88)

    def test_equals_3(self):
        self.assertEqual(total_kilometers(22, 28), 127.27)

    def test_equals_4(self):
        self.assertEqual(check_distance(700, 10, 60), 'You will need to refuel')

    def test_equals_5(self):
        self.assertEqual(check_distance(467, 12.3, 60), [
            [0, 467, 60], [100, 367, 47.7], [200, 267, 35.40],
            [300, 167, 23.10], [400, 67, 10.80]
        ])


if __name__ == '__main__':
    unittest.main()
