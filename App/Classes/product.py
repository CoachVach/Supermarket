from ..Interfaces.Map.product import ProductInterface
from ..Helpers.Constants.interface import *

class Product:
    def __init__(self, name, market_price, color=BLUE, selection=5):
        self.name = name
        self.price = market_price
        self.market_price = market_price
        self.stock = 0
        self.selection = selection
        self.interface = ProductInterface(color)

    def set_price(self, amount):
        self.price = amount

    def add_stock(self,amount):
        self.stock += amount

    def cost(self):
        return self.selection * self.market_price

    def remove_stock(self,amount):
        if (self.stock - amount) >= 0:
            self.stock -= amount
            return True
        else:
            return False

    def is_empty(self):
        return self.stock == 0

    def increment_selection(self):
        if self.selection < 99:
            self.selection += 1

    def decrement_selection(self):
        if self.selection > 1:
            self.selection -= 1

    def draw(self, screen, position):
        self.interface.draw(screen, position)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Market Price: ${self.market_price}, Stock: {self.stock}"