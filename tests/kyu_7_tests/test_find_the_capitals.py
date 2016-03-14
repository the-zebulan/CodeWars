import unittest

from katas.kyu_7.find_the_capitals import capitals


class CapitalsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(capitals('CoDeWaRs'), [0, 2, 4, 6])


if __name__ == '__main__':
    unittest.main()
