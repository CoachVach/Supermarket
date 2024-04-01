import pygame

from App.Classes.position import Position
from App.Helpers.interface_tools import display_custom_text

from ...Helpers.Constants.interface import *

class BoxInterface:
    def __init__(self, x, y = SCREEN_HEIGHT - BOX_HEIGHT*2):
        self.position = Position(x, y, BOX_WIDTH, BOX_HEIGHT)
        self.image = pygame.transform.scale(pygame.image.load("Images/box.png").convert_alpha(), (self.position.width, self.position.height))

    def draw(self, screen, product):
        screen.blit(self.image, (self.position.x, self.position.y))

        product_position = Position(self.position.x + BOX_WIDTH / 4, self.position.y + BOX_HEIGHT / 4, BOX_WIDTH / 2, BOX_HEIGHT / 2)

        product.draw(screen, product_position)

        circle_center = (self.position.x + BOX_WIDTH, self.position.y)
        circle_radius = 12
        pygame.draw.circle(screen, BLACK, circle_center, circle_radius,0)

        display_custom_text(screen, str(product.in_box), 20, WHITE, (self.position.x + BOX_WIDTH - circle_radius/2, self.position.y - circle_radius/2))

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.position.width, self.position.height)
