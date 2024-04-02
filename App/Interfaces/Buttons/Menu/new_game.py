
from App.Helpers.Constants.interface import *
from App.Interfaces.Buttons.button import Button


class NewGameButton(Button):
    
    def __init__(self, screen, x=MENU_BUTTON_X, y=MENU_BUTTON_Y, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT):
        super().__init__(screen, x, y, width, height, WHITE, GREEN, "NEW GAME", font_size=78)