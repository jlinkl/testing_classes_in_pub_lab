import unittest
from src.food import Food

class FoodTest(unittest.TestCase):
    def setUp(self):
        self.food = Food("Pie", 2.00, -3)
        self.food1 = Food("Pizza" , 7, -10)

    def test_drink_name(self):
        self.assertEqual("Pie", self.food.name)

    def test_food_rejuvination_level(self):
        self.assertEqual(-10, self.food1.rejuvination_level)
        
    def test_food_price(self):
        self.assertEqual(2.00, self.food.price)