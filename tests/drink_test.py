import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("beer", 4.50, 2)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink_1.price)

    def test_drink_has_alchol_level(self):
        self.assertEqual(2, self.drink_1.alchol_level)

