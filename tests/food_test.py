import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("burger", 10, -5)
    def test_food_has_name(self):
        self.assertEqual("burger", self.food_1.name)

    def test_food_has_price(self):
        self.assertEqual(10, self.food_1.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(-5, self.food_1.rejuvenation_level)
        self.assertEqual(True, self.food_1.rejuvenation_level < 0)