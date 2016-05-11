import unittest
from datetime import datetime

from katas.kyu_5.mongodb_objectid import Mongo


class MongoDbObjectIdTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(Mongo.is_valid('507f1f77bcf86cd799439011'))

    def test_true_2(self):
        self.assertTrue(Mongo.is_valid('111111111111111111111111'))

    def test_false_1(self):
        self.assertFalse(Mongo.is_valid('507f1f77bcf86cz799439011'))

    def test_false_2(self):
        self.assertFalse(Mongo.is_valid('507f1f77bcf86cd79943901'))

    def test_false_3(self):
        self.assertFalse(Mongo.is_valid(111111111111111111111111))

    def test_false_4(self):
        self.assertFalse(Mongo.is_valid('507f1f77bcf86cD799439011'))

    def test_false_5(self):
        self.assertFalse(Mongo.get_timestamp(False))

    def test_false_6(self):
        self.assertFalse(Mongo.get_timestamp([]))

    def test_false_7(self):
        self.assertFalse(Mongo.get_timestamp(1234))

    def test_false_8(self):
        self.assertFalse(Mongo.get_timestamp('123476sd'))

    def test_false_9(self):
        self.assertFalse(Mongo.get_timestamp('507f1f77bcf86cd79943901'))

    def test_equal_1(self):
        self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd799439016'),
                         datetime(2012, 10, 17, 21, 13, 27))


if __name__ == '__main__':
    unittest.main()
