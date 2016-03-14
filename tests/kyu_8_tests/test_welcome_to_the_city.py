import unittest

from kyu_8.welcome_to_the_city import say_hello


class SayHelloTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(say_hello(
            ['John', 'Smith'], 'Phoenix', 'Arizona'
        ), 'Hello, John Smith! Welcome to Phoenix, Arizona!')

    def test_equals_2(self):
        self.assertEqual(say_hello(
            ['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois'
        ), 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')

    def test_equals_3(self):
        self.assertEqual(say_hello(
            ['Wallace', 'Russel', 'Osbourne'], 'Albany', 'New York'
        ), 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')


if __name__ == '__main__':
    unittest.main()
