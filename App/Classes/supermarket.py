import random

from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import *
from App.Interfaces.Messages.temp_message import TempMessage

class Supermarket:

    def __init__(self, stock, money=100):
        self.stock = stock
        self.money = money

        self.sound = "Sounds/sell.mp3"

    def buy_product(self, product):

        if self.can_buy(product):
            self.money -= product.cost()
            self.stock.add_product(product, product.selection)
            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.play()
            cost = "{:.2f}".format(product.cost())
            return True, TempMessage(f"-${cost}", (TEMP_MONEY_MESSAGE_X, TEMP_MONEY_MESSAGE_Y), RED)
        else:
            return False, None

    def sell_product(self, product, amount):

        if product.stock >= amount:
            self.stock.remove_product(product, amount)
            self.money += product.price * amount
        else:
            return False

    def purchase(self, purchase):

        for product_tuple in purchase.products:
            self.sell_product(product_tuple[0], product_tuple[1])
        
        cost = "{:.2f}".format(purchase.total_cost())
    
        return TempMessage(f"+${cost}", (TEMP_MONEY_MESSAGE_X, TEMP_MONEY_MESSAGE_Y), GREEN)

    def can_buy(self, product):
        return self.money >= product.cost()

    def __str__(self):
        return f"Money: ${self.money} \nStock: \n {self.stock}" 