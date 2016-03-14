import unittest

from katas.kyu_8.lightsabers import howManyLightsabersDoYouOwn


class LightsabersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(howManyLightsabersDoYouOwn('Zach'), 18)

    def test_equals_2(self):
        self.assertEqual(howManyLightsabersDoYouOwn('Jim'), 0)


if __name__ == '__main__':
    unittest.main()
