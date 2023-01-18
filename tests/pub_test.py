import unittest
from src.classes.pub import Pub
from src.classes.customer import Customer
from src.classes.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drinks = Drinks("Tennents", 5.00)
        self.customer = Customer( "David", 69.00, 16)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        drink = Drinks("Tennents", 5.00)
        # expected = 102.50
        self.pub.increase_till(drink)
        # actual = self.pub.till
        # self.assertEqual(expected, actual)
        self.assertEqual(105.00, self.pub.till)

    def test_buy_drink(self):
        self.pub.buy_drink(self.customer, self.drinks)
        self.assertEqual(64, self.customer.wallet)
        self.assertEqual(105.00, self.pub.till)

    def test_check_age(self):
        # age_check = self.pub.check_age(self.customer)
        self.assertEqual(False)