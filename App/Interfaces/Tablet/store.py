import pygame
from App.Helpers.Constants.interface import *
from .product_interface_helper import *
from ..Buttons.exit_button import *

class StoreInterface:

    def __init__(self, store, supermarket):
        self.store = store
        self.supermarket = supermarket

    def show(self, screen, button_clicked, mouse_pos, interface_objects):

        pygame.draw.rect(screen, GRAY, (TABLET_OFFSET, TABLET_OFFSET, SCREEN_WIDTH - 2*TABLET_OFFSET, SCREEN_HEIGHT - 2*TABLET_OFFSET))

        i = 0
        for product in self.store.products:

            draw_product(product, screen, button_clicked, mouse_pos, i, self, interface_objects)

            i += 1

        exit_store = interface_objects.exit_button.draw(mouse_pos, button_clicked)

        return not exit_store

    def buy_product(self, product):
        return self.supermarket.buy_product(product)
