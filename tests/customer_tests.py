import unittest
from src.classes.pub import Pub
from src.classes.customer import Customer
from src.classes.drinks import Drinks

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer( "David", 69.00, 16)
        self.pub = Pub("The Prancing Pony", 100.00)
    

    def test_customer_has_name(self):
        self.assertEqual("David", self.customer.name)

    def test_reduce_wallet(self):
        drink = Drinks("Tennents" , 5.00)
        self.customer.reduce_wallet(drink)
        self.assertEqual(64.00, self.customer.wallet)

