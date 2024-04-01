import pygame
from ...Helpers.Constants.interface import *

class ProductInterface():

    def __init__(self, color, image=None):
        self.image = pygame.image.load(PRODUCT_IMAGE_PATH + image).convert_alpha()
        self.color = color

    def draw(self, screen, position):
        scaled_image = pygame.transform.scale(self.image, (position.width, position.height)).convert_alpha()
        screen.blit(scaled_image, (position.x, position.y))