import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drinks = {"beer": 10, "wine": 10, "rum": 5, "gin": 0}
        self.pub = Pub("chanter", 100.00, drinks)

        self.drink_1 = Drink("beer", 4.50, 2) #value = £45
        self.drink_2 = Drink("wine", 5.00, 3) #value = £50
        self.drink_3 = Drink("rum", 6.00, 4) #value = £30
        self.drink_4 = Drink("gin", 8.00, 5) #value = £0
        self.food_1 = Food("burger", 10, -5)

    def test_pub_has_name(self):
        self.assertEqual("chanter", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        drinks = {"beer": 10, "wine": 10, "rum": 5, "gin": 0}
        self.assertEqual(drinks, self.pub.drinks)
    
    def test_pub_has_stock(self):
        self.assertEqual(25, self.pub.stock)

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110.00, self.pub.till)
    
    def test_reduce_drinks_stock(self):
        self.pub.reduce_drinks_stock("beer")
        self.assertEqual(9, self.pub.drinks["beer"])

    def test_get_stock_value(self):
        stock_of_beer = self.pub.get_stock_value("beer")
        self.assertEqual(10, stock_of_beer)

    def test_sell_drink__old_enough(self):
        customer_1 = Customer("steve", 10.00, 18, 2)
        self.pub.sell_drink(customer_1, self.drink_1)
        self.assertEqual(5.50, customer_1.wallet)
        self.assertEqual(104.50, self.pub.till)
        self.assertEqual(4, customer_1.drunkenness)
        self.assertEqual(9, self.pub.drinks[self.drink_1.name])

    def test_sell_drink__too_young(self):
        customer_2 = Customer("dave", 10.00, 16, 0)
        self.pub.sell_drink(customer_2, self.drink_1)
        self.assertEqual(10, customer_2.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(0, customer_2.drunkenness)
        self.assertEqual(10, self.pub.drinks[self.drink_1.name])

    def test_sell_drink__too_drunk(self):
        customer_3 = Customer("natalie", 10.00, 20, 15)
        self.pub.sell_drink(customer_3, self.drink_1)
        self.assertEqual(10, customer_3.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(15, customer_3.drunkenness)
        self.assertEqual(10, self.pub.drinks[self.drink_1.name])
    
    def test_sell_drink__no_stock(self):
        customer_4 = Customer("alan", 15.00, 25, 2)
        self.pub.sell_drink(customer_4, self.drink_4)
        self.assertEqual(15, customer_4.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(2, customer_4.drunkenness)
        self.assertEqual(0, self.pub.drinks[self.drink_4.name])

    def test_sell_food(self):
        customer_5 = Customer("megan", 20.00, 18, 2)
        self.pub.sell_food(customer_5, self.food_1)
        self.assertEqual(10, customer_5.wallet)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(0, customer_5.drunkenness)
    
    def test_stock_value(self):
        drinks_list = [self.drink_1, self.drink_2, self.drink_3]
        total_value = self.pub.stock_value(drinks_list)
        self.assertEqual(125.00, total_value)
