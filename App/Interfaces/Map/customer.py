import pygame

from App.Classes.position import Position
from App.Helpers.Constants.interface import *

class CustomerInterface:
    
    def __init__(self):
        self.position = Position(100, 400, CUSTOMER_WIDTH, CUSTOMER_HEIGHT)
        self.color = CUSTOMER_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, self.position.width, self.position.height))