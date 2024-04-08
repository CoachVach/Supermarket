from ..Interfaces.Map.product import ProductInterface
from ..Helpers.Constants.interface import *

class Product:
    def __init__(self, name, sell_price, image="", selection=5):
        self.name = name
        self.price = sell_price
        self.sell_price = sell_price
        self.market_price = sell_price * 1.15
        self.stock = 0
        self.in_box = 0
        self.selection = selection

        self.image = image
        self.interface = ProductInterface(image)

    def set_price(self, amount):
        self.price = amount

    def add_stock(self,amount):
        self.stock += amount
        self.in_box += amount

    def cost(self):
        return self.selection * self.sell_price

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

    def decrement_price(self):
        if self.price > 0.10:
            self.price -= 0.10

    def increment_price(self):
        if self.price < 99:
            self.price += 0.10

    def draw(self, screen, position):
        self.interface.draw(screen, position)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Market Price: ${self.sell_price}, Stock: {self.stock}"