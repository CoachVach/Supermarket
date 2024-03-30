import pygame
from App.Classes.position import Position
from App.Helpers.Constants.interface import *


class CashRegisterInterface:
    def __init__(self):
        self.position = Position(CASH_REGISTER_X, CASH_REGISTER_Y, CASH_REGISTER_WIDTH, CASH_REGISTER_HEIGHT)
        self.image =  pygame.transform.scale(pygame.image.load(PRODUCT_IMAGE_PATH + "cash_register.png").convert_alpha(), (self.position.width, self.position.height))

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))