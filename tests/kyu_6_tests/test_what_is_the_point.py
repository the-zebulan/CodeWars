import unittest

from kyu_6.what_is_the_point import pointless


class PointlessTestCase(unittest.TestCase):
    def setUp(self):
        self.nums = (
            60, 97, 32, 115, 116, 121, 108, 101, 61, 34, 99, 111, 108, 111,
            114, 58, 119, 104, 105, 116, 101, 59, 34, 32, 104, 114, 101, 102,
            32, 61, 34, 104, 116, 116, 112, 115, 58, 47, 47, 119, 119, 119,
            46, 121, 111, 117, 116, 117, 98, 101, 46, 99, 111, 109, 47, 119,
            97, 116, 99, 104, 63, 118, 61, 54, 45, 72, 85, 103, 122, 89, 80,
            109, 57, 103, 34, 62, 87, 101, 108, 108, 32, 100, 111, 110, 101,
            33, 32, 87, 104, 111, 32, 105, 115, 32, 116, 104, 101, 32, 103,
            117, 121, 32, 105, 110, 32, 116, 104, 101, 32, 104, 111, 108, 111,
            103, 114, 97, 109, 63, 60, 47, 97, 62
        )

    def test_equals(self):
        self.assertEqual(''.join(chr(a) for a in self.nums),
                         '<a style="color:white;" href ="https://www.youtube'
                         '.com/watch?v=6-HUgzYPm9g">Well done! Who is the gu'
                         'y in the hologram?</a>')

    def test_equals_2(self):
        self.assertEqual(pointless(), 'Rick Astley')


if __name__ == '__main__':
    unittest.main()
