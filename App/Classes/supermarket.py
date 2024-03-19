import random

class Supermarket:

    def __init__(self, stock, customers=[], money=100):
        self.stock = stock
        self.money = money
        self.customers = customers

    def buy_product(self, product):

        if self.can_buy(product):
            self.money -= product.cost()
            self.stock.add_product(product, product.selection)
            return True
        else:
            return False

    def sell_product(self, product, amount):

        if product.stock >= amount:
            self.stock.remove_product(product, amount)
            self.money += product.price * amount
        else:
            return False

    def purchase(self):

        customer = random.choice(self.customers)

        purchase = customer.buy(self.stock.products)

        for product_tuple in purchase.products:
            self.sell_product(product_tuple[0], product_tuple[1])

    def can_buy(self, product):
        return self.money >= product.cost()

    def __str__(self):
        return f"Money: ${self.money} \nStock: \n {self.stock}" 