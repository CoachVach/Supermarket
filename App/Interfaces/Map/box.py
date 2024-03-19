import pygame

from App.Classes.position import Position

from ...Helpers.Constants.interface import *

class BoxInterface:
    def __init__(self, x, y):
        self.position = Position(x, y, BOX_WIDTH, BOX_HEIGHT)
        self.color = BOX_COLOR

    def draw(self, screen, product):
        if not product:
            color = RED
        else:
            color = self.color
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, self.position.width, self.position.height))

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.position.width, self.position.height)
