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
        for p in products:
            total += p[0].price * p[1]
        
        return total
    
    def add_product(self, product, amount):

        prod_tuple = [product, amount]

        self.products.append(prod_tuple)

    def more_products_allowed(self):

        max_products_reached = self.amount_products() >= MAX_PRODUCTS
        max_unique_products_reached = self.amount_unique_products() >= MAX_UNIQUE_PRODUCTS

        return (not max_products_reached) and (not max_products_reached)

    def __str__(self):

        string = f"Purchase: Total cost = ${self.total_cost()}\nTotal products = {self.amount_products()}\nUnique products = {self.amount_unique_products()}\nProducts:\n "

        for product in self.products:
            string += str(product) + "\n "

        return string