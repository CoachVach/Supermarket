
from App.Helpers.interface_tools import display_text

class TempMessage:
    def __init__(self, text, position, color):
        self.x, self.y = position
        self.color = color
        self.text = text

        self.frames = 15

    def draw(self, screen):
        display_text(screen, self.text, self.color, (self.x, self.y))
        self.frames -= 1
        self.y -= 15 - self.frames

        if self.frames == 0:
            return False
        else:
            return True