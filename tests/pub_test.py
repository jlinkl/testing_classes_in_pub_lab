import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        
        self.customer = Customer(50.00, 0, 20)
        self.customer1 = Customer(20.00, 0, 17)
        
        self.drink = Drink("Guiness", 5.00, 4, 2)
        self.drink1 = Drink("Tennents", 4.50, 3, 1)
        self.drink2 = Drink("Rum", 6.00, 6, 1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertIsNot(0, len(self.pub.drinks))
        print(self.pub.stock)

    def test_check_age(self):
        age = self.customer.age
        self.assertEquals(True, self.pub.check_age(age))

    def test_can_serve(self):
        self.assertEqual(True, self.pub.can_serve(self.customer))

    def test_stock(self):
        self.assertEqual(2, self.drink.stock)

    def test_stock_value(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(2, self.pub.stock_value())
    

