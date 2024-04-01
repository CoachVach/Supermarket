import pygame
from App.Helpers.Constants.interface import *
from .product_interface_helper import *
from ..Buttons.exit_button import *

class StockInterface:

    def __init__(self, stock):
        self.stock = stock

    def show(self, screen, button_clicked, mouse_pos):

        pygame.draw.rect(screen, GRAY, (TABLET_OFFSET, TABLET_OFFSET, SCREEN_WIDTH - 2*TABLET_OFFSET, SCREEN_HEIGHT - 2*TABLET_OFFSET))

        i = 0
        if self.stock.products == []:
            self.display_no_products(screen)
        else:
            for product in self.stock.products:

                draw_product_in_stock(product, screen, button_clicked, mouse_pos, i)

                i += 1

        exit_store = self.stock.interface_objects.exit_button.draw(mouse_pos, button_clicked)

        return not exit_store

    def display_no_products(self, screen):
        font = pygame.font.Font(None, 60)  # You can change the font and size hereext
        text = "NO PRODUCTS"

        text_surface = font.render(text, True, DARK_GRAY)
        text_rect = text_surface.get_rect()

        # Calculate the position to center the text in the middle of the screen
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        screen.blit(text_surface, text_rect)