

from App.Interfaces.Map.box import BoxInterface

class Box():

    def __init__(self, product=None, amount=0, x=50):
        self.product = product
        self.amount = amount
        self.interface = BoxInterface(x)

    def get_product(self, capacity):
        amount = 0
        if self.amount > 0:
            if self.amount > capacity:
                amount = capacity
            else:
                amount = self.amount

        self.amount -= amount

        product = self.product

        if self.amount == 0:
            self.product = None

        return product, amount
    
    def draw(self, screen):
        if self.amount > 0:
            self.interface.draw(screen, self.product)
            return False
        else:
            return True
