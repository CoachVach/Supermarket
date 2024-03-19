
import random

from .purchase import Purchase
from .position import Position

class Customer:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.position = Position()

    def buy(self, products):

        purchase = Purchase()

        while purchase.more_products_allowed():

            product, amount = self.choose_product(products)
            purchase.add_product(product, amount)

        return purchase

    def choose_product(self, products):
        product = random.choice(products)
        amount = random.randint(1, min(product.stock, 3))

        return product, amount

    def __str__(self):
        return f"Customer: Name = {self.name}, Money = {self.money}"