from .Buttons.add_shelf import *
from .Buttons.exit_button import *

class InterfaceObjects:
    def __init__(self, screen, shelves=[], boxes=[]):
        self.screen = screen

        self.shelves = shelves
        
        self.add_shelf_button = AddShelfButton(screen)

        self.boxes = boxes

        self.exit_button = ExitButton(screen)

        self.temp_message = None

    def draw(self, mouse_pos, button_clicked):
        for shelf in self.shelves:
            shelf.draw(self.screen, mouse_pos, button_clicked)

        for box in self.boxes:
            delete = box.draw(self.screen)
            if delete:
                self.boxes.remove(box)

        self.draw_temps()

    def draw_temps(self):
        if self.temp_message != None:
            if not self.temp_message.draw(self.screen):
                self.temp_message = None

    def shelf_position(self, product):
        for shelf in self.shelves:
            if shelf.product == product:
                return shelf, (shelf.interface.position.rect().centerx, shelf.interface.position.rect().centery)
            
        return None, None
    
    def products_in_shelfs(self):
        products = []
        for shelf in self.shelves:
            if (shelf.product not in products) and (shelf.product != None):
                products.append(shelf.product)
        return products
    
    def get_shelf(self, point):
        for shelf in self.shelves:
            if shelf.interface.position.rect().collidepoint(point):
                return shelf

        return None