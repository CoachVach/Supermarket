import pygame
from ...Helpers.Constants.interface import *

class ProductInterface():

    def __init__(self, color, image=None):
        self.image = image
        self.color = color

    def draw(self, screen, position):
        pygame.draw.rect(screen, self.color, (position.x, position.y, position.width, position.height))

        pygame.draw.rect(screen, BLACK, (position.x, position.y, position.width, position.height),1)