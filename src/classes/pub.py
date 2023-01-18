class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def increase_till(self, drink):
        self.till += drink.price
    
    def buy_drink(self, customer, drink):
        self.increase_till(drink)
        customer.wallet -= drink.price

    def check_age(self, customer):
        if self.customer.age >= 18:
            return True