import unittest

from katas.beta.cycle_through_items import cycle


class CycleTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = [1, 2, None, 3, 4]
        self.lst[2] = self.lst

        self.lst_2 = ['list', {'str': 'dict'}]
        self.lst_2[1]['list'] = self.lst_2

    def test_equal_1(self):
        self.assertEqual(list(cycle(1)), [1])

    def test_equal_2(self):
        self.assertEqual(list(cycle([0, 1, 2, 3])), [0, 1, 2, 3])

    def test_equal_3(self):
        self.assertEqual(list(cycle([])), [])

    def test_equal_4(self):
        self.assertEqual(list(cycle(
            {'A': 'A', 'a': 'a', 'b': 'b', 'X': 'X', 'y': 'y'})),
            ['A', 'X', 'a', 'b', 'y'])

    def test_equal_5(self):
        self.assertEqual(list(cycle(['a', 'b', ['c', 'd', 'e'], 'f', 'g'])),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_equal_6(self):
        self.assertEqual(list(cycle([[1], 2, {3: 3}])), [1, 2, 3])

    def test_equal_7(self):

        self.assertEqual(list(cycle(self.lst)), [1, 2, 3, 4])

    def test_equal_8(self):
        self.assertEqual(list(cycle(self.lst_2)), ['list', 'dict'])

    def test_equal_9(self):
        self.assertEqual(list(cycle(self.lst_2[1])), ['list', 'dict'])
