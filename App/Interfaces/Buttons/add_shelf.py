from ...Helpers.Constants.interface import *
from .button import *

class AddShelfButton(Button):
    
    def __init__(self, screen, x=ADD_SHELF_BUTTON_X, y=ADD_SHELF_BUTTON_Y, width=ADD_SHELF_BUTTON_WIDTH, height=ADD_SHELF_BUTTON_HEIGHT):
        super().__init__(screen, x, y, width, height, GREEN, WHITE, "Buy Shelf")
