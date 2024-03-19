from .Buttons.add_shelf import *
from .Buttons.exit_button import *

class InterfaceObjects:
    def __init__(self, screen, shelves=[], boxes=[]):
        self.screen = screen

        self.shelves = shelves
        
        self.add_shelf_button = AddShelfButton(screen)

        self.boxes = boxes

        self.exit_button = ExitButton(screen)

    def draw(self, mouse_pos, button_clicked):
        for shelf in self.shelves:
            shelf.draw(self.screen, mouse_pos, button_clicked)

        for box in self.boxes:
            delete = box.draw(self.screen)
            if delete:
                self.boxes.remove(box)