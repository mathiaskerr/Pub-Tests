import unittest
from src.classes.pub import Pub
from src.classes.customer import Customer
from src.classes.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Tennents", 5.00)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drinks.name)

    # def test_increase_till(self):
    #     # expected = 102.50
    #     self.pub.increase_till(2.50)
    #     # actual = self.pub.till
    #     # self.assertEqual(expected, actual)
    #     self.assertEqual(102.50, self.pub.till)