import unittest
from src.classes.pub import Pub
from src.classes.customer import Customer
from src.classes.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Tennents", 5.00, 1)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drinks.name)



 