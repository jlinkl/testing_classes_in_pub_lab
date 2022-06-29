import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(50.00, 0, 20)
        self.customer1 = Customer(20.00, 0, 17)

    def test_can_buy_drink(self):
        drink = Drink("Guiness", 5.00, 4)
        self.assertEqual(True, self.customer.check_wallet(drink.price))

    def test_buy_drink(self):
        drink = Drink("Guiness", 5.00, 4)
        pub = Pub("The Prancing Pony", 100.00)
        pub.add_drink(drink)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(True, pub.can_serve(self.customer))
        self.assertEqual(True, self.customer.check_wallet(drink.price))
        self.assertEqual(True, pub.has_drink(drink))
        self.assertEqual(105.00, pub.till)
        self.assertEqual(45.00, self.customer.wallet)

    def test_change_drunkeness(self):
        drink = Drink("Guiness", 5.00, 4)
        self.customer.change_drunkeness(drink)
        self.assertEqual(4, self.customer.drunkeness)


