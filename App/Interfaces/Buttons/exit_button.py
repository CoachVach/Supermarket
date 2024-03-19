from ...Helpers.Constants.interface import *
from .button import *

class ExitButton(Button):

    def __init__(self, screen, x=TABLET_WIDTH + TABLET_OFFSET - EXIT_BUTTON_WIDTH/2, y=TABLET_OFFSET - EXIT_BUTTON_HEIGHT/2, width=EXIT_BUTTON_WIDTH, height=EXIT_BUTTON_HEIGHT):      
        super().__init__(screen, x, y, width, height, RED, RED_GRAY, "X")