from src.pub import Pub

class Customer:
    def __init__(self, wallet, drunkeness, age):
        self.wallet = wallet
        self.drunkeness = drunkeness
        self.age = age

    def check_wallet(self, price):
        if self.wallet < price:
            return False
        else:
            return True

    def take_from_wallet(self, money):
        self.wallet -= money

    def change_drunkeness(self, drink):
        self.drunkeness += drink.alcohol_level

    def buy_drink(self, drink, pub):
        if pub.can_serve(self) and self.check_wallet(drink.price):
            pub.add_to_till(drink.price)
            self.take_from_wallet(drink.price)


