import unittest
from src.classes.pub import Pub
from src.classes.customer import Customer
from src.classes.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drinks = Drinks("Tennents", 5.00, 1)
        self.customer = Customer( "David", 69.00, 18)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(self.drinks)
        self.assertEqual(105.00, self.pub.till)

    def test_buy_drink(self):
        self.pub.buy_drink(self.customer, self.drinks)
        self.assertEqual(64, self.customer.wallet)
        self.assertEqual(105.00, self.pub.till)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer.age))

    def test_sober(self):
        self.assertEqual(True, self.pub.sober(self.customer.drunk))
    
    def test_buy_drink_with_check(self):
        self.pub.buy_drink_with_check(self.customer, self.drinks)
        self.assertEqual(64, self.customer.wallet)
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(1, self.customer.drunk)
        self.assertEqual(True, self.pub.check_age(self.customer.age))
        self.assertEqual(True, self.pub.sober(self.customer.drunk))