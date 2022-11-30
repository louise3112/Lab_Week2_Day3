import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

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

    def test_sell_drink__old_enough(self):
        customer_1 = Customer("steve", 10.00, 18, 2)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_1, drink_1)
        self.assertEqual(5.50, customer_1.wallet)
        self.assertEqual(104.50, self.pub.till)
        self.assertEqual(4, customer_1.drunkenness)

    def test_sell_drink__too_young(self):
        customer_2 = Customer("dave", 10.00, 16, 0)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_2, drink_1)
        self.assertEqual(10, customer_2.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(0, customer_2.drunkenness)

    def test_sell_drink__too_drunk(self):
        customer_3 = Customer("dave", 10.00, 20, 15)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_3, drink_1)
        self.assertEqual(10, customer_3.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(15, customer_3.drunkenness)

    def test_sell_food(self):
        customer_1 = Customer("steve", 20.00, 18, 2)
        food_1 = Food("burger", 10, -5)
        self.pub.sell_food(customer_1, food_1)
        self.assertEqual(10, customer_1.wallet)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(0, customer_1.drunkenness)

