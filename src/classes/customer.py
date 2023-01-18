class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        drunkness = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price
    
