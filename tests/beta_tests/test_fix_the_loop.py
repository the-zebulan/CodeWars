import unittest

from katas.beta.fix_the_loop import list_animals


class ListAnimalsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(list_animals(['dog', 'cat', 'elephant']),
                         '1. dog\n2. cat\n3. elephant\n')
