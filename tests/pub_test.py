import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drinks = ["beer", "wine", "coke"]
        self.pub = Pub("chanter", 100.00, drinks)

    def test_pub_has_name(self):
        self.assertEqual("chanter", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        drinks = ["beer", "wine", "coke"]
        self.assertEqual(drinks, self.pub.drinks)