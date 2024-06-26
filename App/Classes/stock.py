from App.Classes.box import Box
from App.Helpers.Constants.interface import BOX_WIDTH

class Stock:
    
    def __init__(self, products=[], interface_objects=None):
        self.products = products
        self.interface_objects = interface_objects

    def add_product(self, product, amount):
        product.add_stock(amount)
        if product not in self.products:
            self.products.append(product)
        
        box = self.box_of_product(product)
        if box != None:
            box.amount += amount
        else:
            box_x = 50 + BOX_WIDTH*len(self.interface_objects.boxes)
            self.interface_objects.boxes.append(Box(product, amount, box_x))

    def remove_product(self, product, amount):
        product.remove_stock(amount)

        if product.is_empty():
            self.remove_from_stock(product)

    def remove_from_stock(self, product):
        if self.product_in_stock(product):
            self.products.remove(product)
            return True
        return False

    def product_in_stock(self, product):
        return product in self.products
    
    def box_of_product(self, product):
        for box in self.interface_objects.boxes:
            if box.product == product:
                return box
        
        return None

    def data(self):
        products = []
        for product in self.products:
            products.append((product.name, product.price))
        return products
    
    def __str__(self):
        string = ""
        for product in self.products:
            string += str(product) + "\n "
        return string