
from App.Helpers.Constants.interface import *
from App.Interfaces.Buttons.button import Button


class SaveButton(Button):
    
    def __init__(self, screen, x=MENU_BUTTON_X, y=MENU_BUTTON_Y + (MENU_BUTTON_HEIGHT + MENU_BUTTON_OFFSET), width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT):
        super().__init__(screen, x, y, width, height, WHITE, GREEN, "SAVE GAME", font_size=78)