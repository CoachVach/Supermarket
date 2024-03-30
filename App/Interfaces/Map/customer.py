import pygame

from App.Classes.position import Position
from App.Helpers.Constants.interface import *

class CustomerInterface:
    
    def __init__(self):
        self.position = Position(100, 400, CUSTOMER_WIDTH, CUSTOMER_HEIGHT)
        self.image = pygame.transform.scale(pygame.image.load(CUSTOMER_IMAGE_PATH + "customer_1.png").convert_alpha(), (self.position.width, self.position.height))

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))