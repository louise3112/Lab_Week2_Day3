import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

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

    def test_add_money(self):
        self.pub.add_money(10)
        self.assertEqual(110.00, self.pub.till)

    def test_buy_drink(self):
        customer_1 = Customer("steve", 10.00)
        drink_1 = Drink("beer", 4.50)
        self.pub.buy_drink(customer_1, drink_1)
        self.assertEqual(5.50, customer_1.wallet)
        self.assertEqual(104.50, self.pub.till)