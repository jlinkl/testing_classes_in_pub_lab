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

    

    

