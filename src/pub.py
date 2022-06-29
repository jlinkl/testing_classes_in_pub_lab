class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    def check_age(self, age):
        if age < 18:
            return False
        else:
            return True

    def check_drunkeness(self, drunkeness):
        if drunkeness > 20:
            return False
        else:
            return True

    def can_serve(self, customer):
        if self.check_age(customer.age) and self.check_drunkeness(customer.drunkeness):
            return True
        else:
            return False

    def add_drink(self, drink):
        self.drinks.append(drink)
        self.stock[drink.name] = drink.stock

    def add_to_till(self, price):
        self.till += price

    def has_drink(self, drink):
        if self.stock.get(drink.name):
            return True
        else:
            return False

    def stock_value(self):
        total = 0
        for drink in self.drinks:
            total += self.stock.get(drink.name)
        return total







