import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("steve", 10.00)
    def test_customer_has_name(self):
        self.assertEqual("steve", self.customer_1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer_1.wallet)