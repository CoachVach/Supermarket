import random

from ..Helpers.Constants.logic import MAX_PRODUCTS, MAX_UNIQUE_PRODUCTS

class Purchase:
    
    def __init__(self,):
        self.products = []

    def amount_unique_products(self):
        return len(self.products)

    def amount_products(self):
        return sum(product[1] for product in self.products)

    def total_cost(self):
        total = 0
        for p in self.products:
            total += p[0].price * p[1]
        
        return total
    
    def add_product(self, product, amount):

        chance = self.calculate_chance(product)

        if random.random() > chance:
            amount = 0
        prod_tuple = [product, amount]

        self.products.append(prod_tuple)

        return amount

    def more_products_allowed(self):

        max_products_reached = self.amount_products() >= MAX_PRODUCTS
        max_unique_products_reached = self.amount_unique_products() >= MAX_UNIQUE_PRODUCTS

        return (not max_products_reached) and (not max_unique_products_reached)
    
    def calculate_chance(self, product):
        difference = product.price - product.market_price

        if difference > 0:
            if difference < product.market_price*0.1:
                base = 0.75 # 11-10 = 1     1 / (1-(1/1))
                offset = (product.market_price*0.1 - (1-(difference / (product.market_price*0.1)))) * 0.15 
            elif difference < product.market_price*0.2:
                base = 0.4 
                difference = difference - product.market_price*0.1
                offset = (product.market_price*0.1 - (1-(difference / (product.market_price*0.1)))) * 0.25
            elif difference < product.market_price*0.3:
                base = 0.1
                difference = difference - product.market_price*0.2
                offset = (product.market_price*0.1 - (1-(difference / (product.market_price*0.1)))) * 0.25
            else:
                base = 0
                offset = 0

        else:
            base = 0.9
            difference *= -1

            if difference > product.market_price*0.1:
                offset = 0.1
            else:
                offset = (difference / product.market_price)

        chance = base + offset

        return chance

    def __str__(self):

        string = f"Purchase: Total cost = ${self.total_cost()}\nTotal products = {self.amount_products()}\nUnique products = {self.amount_unique_products()}\nProducts:\n "

        for product in self.products:
            string += str(product) + "\n "

        return string