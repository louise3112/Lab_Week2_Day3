import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("steve", 10.00)
    def test_customer_has_name(self):
        self.assertEqual("steve", self.customer_1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer_1.wallet)

    def test_take_money(self):
        self.customer_1.take_money(5.00)
        self.assertEqual(5.00, self.customer_1.wallet)

    