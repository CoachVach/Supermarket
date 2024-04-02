
from App.Helpers.Constants.interface import *
from App.Interfaces.Buttons.button import Button


class SettingsButton(Button):
    
    def __init__(self, screen, x=MENU_BUTTON_X, y=MENU_BUTTON_Y + (MENU_BUTTON_HEIGHT + MENU_BUTTON_OFFSET)*3, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT):
        super().__init__(screen, x, y, width, height, WHITE, GREEN, "SETTINGS", font_size=78)