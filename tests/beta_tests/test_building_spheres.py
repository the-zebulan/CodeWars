import unittest

from beta.building_spheres import Sphere


class SphereTestCase(unittest.TestCase):
    def setUp(self):
        self.ball = Sphere(2, 50)

    def test_equals(self):
        self.assertEqual(self.ball.get_radius(), 2)

    def test_equals_2(self):
        self.assertEqual(self.ball.get_mass(), 50)

    def test_equals_3(self):
        self.assertEqual(self.ball.get_volume(), 33.51032)

    def test_equals_4(self):
        self.assertEqual(self.ball.get_surface_area(), 50.26548)

    def test_equals_5(self):
        self.assertEqual(self.ball.get_density(), 1.49208)


if __name__ == '__main__':
    unittest.main()
