import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drinks = {"beer": 10, "wine": 10, "rum": 5}
        self.pub = Pub("chanter", 100.00, drinks)

    def test_pub_has_name(self):
        self.assertEqual("chanter", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        drinks = {"beer": 10, "wine": 10, "rum": 5}
        self.assertEqual(drinks, self.pub.drinks)
    
    def test_pub_has_stock(self):
        self.assertEqual(25, self.pub.stock)

    def test_add_money(self):
        self.pub.add_money(10)
        self.assertEqual(110.00, self.pub.till)
    
    def test_reduce_drinks_stock(self):
        self.pub.reduce_drinks_stock("beer")
        self.assertEqual(9, self.pub.drinks["beer"])

    def test_sell_drink__old_enough(self):
        customer_1 = Customer("steve", 10.00, 18, 2)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_1, drink_1)
        self.assertEqual(5.50, customer_1.wallet)
        self.assertEqual(104.50, self.pub.till)
        self.assertEqual(4, customer_1.drunkenness)
        self.assertEqual(9, self.pub.drinks["beer"])

    def test_sell_drink__too_young(self):
        customer_2 = Customer("dave", 10.00, 16, 0)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_2, drink_1)
        self.assertEqual(10, customer_2.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(0, customer_2.drunkenness)
        self.assertEqual(10, self.pub.drinks["beer"])

    def test_sell_drink__too_drunk(self):
        customer_3 = Customer("natalie", 10.00, 20, 15)
        drink_1 = Drink("beer", 4.50, 2)
        self.pub.sell_drink(customer_3, drink_1)
        self.assertEqual(10, customer_3.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(15, customer_3.drunkenness)
        self.assertEqual(10, self.pub.drinks["beer"])

    def test_sell_food(self):
        customer_4 = Customer("megan", 20.00, 18, 2)
        food_1 = Food("burger", 10, -5)
        self.pub.sell_food(customer_4, food_1)
        self.assertEqual(10, customer_4.wallet)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(0, customer_4.drunkenness)
    
    def test_stock_value(self):
        drink_1 = Drink("beer", 4.50, 2) #£45
        drink_2 = Drink("wine", 5.00, 3) #£50
        drink_3 = Drink("rum", 6.00, 4) #£30
        drinks_list = [drink_1, drink_2, drink_3]
        total_value = self.pub.stock_value(drinks_list)
        self.assertEqual(125.00, total_value)
