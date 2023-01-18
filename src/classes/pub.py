class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def increase_till(self, drink):
        self.till += drink.price
    
    def buy_drink(self, customer, drink):
        self.increase_till(drink)
        customer.wallet -= drink.price

    def check_age(self, age):
        return age >= 18

    def sober(self, drunk):
        return drunk <= 10
        
    def buy_drink_with_check(self, customer, drink):
        if self.check_age(customer.age) and self.sober(customer.drunk):
            self.buy_drink(customer, drink)
            customer.increase_drunk(drink.alcohol_level)
        else:
            return "You are too drunk to serve"    


            



            
