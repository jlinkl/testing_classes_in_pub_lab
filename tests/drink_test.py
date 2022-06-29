import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 5.00, 4, 2)
        self.drink1 = Drink("Tennents", 4.50, 3, 1)
        self.drink2 = Drink("Rum", 6.00, 6, 1)

    def test_drink_name(self):
        self.assertEqual("Guiness", self.drink.name)

    def test_drink_alcohol_level(self):
        self.assertEqual(4, self.drink.alcohol_level)

    def test_drink_price(self):
        self.assertEqual(5.00, self.drink.price)