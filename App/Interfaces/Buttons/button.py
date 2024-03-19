import pygame

from ...Helpers.Constants.interface import *
from ...Classes.position import *
from ...Helpers.interface_tools import *

class Button:
    def __init__(self, screen, x=0, y=0, width=10, height=10, color=GRAY, hover_color=WHITE, text="", text_color=BLACK):
        self.screen = screen

        self.position = Position(x, y, width, height)

        self.color = color

        self.hover_color = hover_color

        self.text = text

        self.text_color = text_color

    def draw(self, mouse_pos, button_clicked):

        color = self.color

        if self.rect().collidepoint(mouse_pos):
            color = self.hover_color
            if button_clicked:
                return True

        pygame.draw.rect(self.screen, color, self.rect())

        display_text(self.screen, self.text, self.text_color, (self.position.x + TEXT_OFFSET, self.position.y + TEXT_OFFSET))

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.position.width, self.position.height) 