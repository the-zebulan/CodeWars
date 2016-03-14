import unittest

from katas.kyu_8.grasshopper_debug import weather_info


class WeatherInformationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(weather_info(50),
                         '10.0 is above freezing temperature')

    def test_equals_2(self):
        self.assertEqual(weather_info(23), '-5.0 is freezing temperature')


if __name__ == '__main__':
    unittest.main()
