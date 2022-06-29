import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 5.00, 4)
        self.drink1 = Drink("Tennents", 4.50, 3)
        self.drink2 = Drink("Rum", 6.00, 6)
        self.drink3 = Drink("Water", 0.00, 0)