class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

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

    def add_to_till(self, price):
        self.till += price

    def has_drink(self, drink):
        for dri in self.drinks:
            if dri == drink:
                return True
        return False