import pygame
from ...Helpers.Constants.interface import *

class ProductInterface():

    def __init__(self, color, image=None):
        self.image = pygame.image.load(IMAGE_PATH + image)
        self.color = color

    def draw(self, screen, position):
        scaled_image = pygame.transform.scale(self.image, (position.width, position.height))
        screen.blit(scaled_image, (position.x, position.y))