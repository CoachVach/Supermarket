from ..Helpers.Constants.interface import *
from ..Helpers.Constants.logic import *

from ..Interfaces.Map.shelf import ShelfInterface

class Shelf:
    
    def __init__(self, product=None, amount=0, capacity=SHELF_CAPACITY):
        self.product = product
        self.amount = amount
        self.capacity = capacity
        self.interface = ShelfInterface()
        self.price = SHELF_PRICE

    def empty(self):
        return self.amount == 0

    def full(self):
        return self.amount == self.capacity

    def cost(self):
        return self.price

    def remove_product(self):

        if not self.empty():
            self.amount -= 1

        if self.empty():
            self.product = None

    def add_product(self, prod):

        if self.product == None:
            self.product = prod
            self.amount += 1
        elif self.product == prod and not self.full():
            self.amount += 1
        else:
            return False

        return True

    def draw(self, screen, button_clicked, mouse_pos):
        self.interface.draw(screen, button_clicked, mouse_pos, self.product, self.amount)

    def editor_mode(self, editor):
        self.interface.editor = editor

    def update_position(self, x, y):
        self.interface.update_position(x, y)

    def orientation(self, vertical):
        self.interface.orientation(vertical)

