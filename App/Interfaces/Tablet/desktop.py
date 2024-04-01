import pygame
from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import *
from ..Buttons.exit_button import *

def tablet_interface(screen, button_clicked, mouse_pos, interface_objects):
    store = False
    tablet = True
    editor = False
    stock = False

    draw_bg(screen)
    store_rect = pygame.Rect(BUTTON_OFFSET + TABLET_OFFSET, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    editor_rect = pygame.Rect(2*BUTTON_OFFSET + TABLET_OFFSET + BUTTON_WIDTH, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    stock_rect = pygame.Rect(3*BUTTON_OFFSET + TABLET_OFFSET + 2*BUTTON_WIDTH, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

    store_color = WHITE
    editor_color = WHITE
    stock_color = WHITE

    if store_rect.collidepoint(mouse_pos):
        if button_clicked:
            store = True
        store_color = RED
    elif editor_rect.collidepoint(mouse_pos):
        if button_clicked:
            editor = True
            tablet = False
            return store, tablet, editor, stock
        editor_color = RED
    elif stock_rect.collidepoint(mouse_pos):
        if button_clicked:
            stock = True
        stock_color = RED

    pygame.draw.rect(screen, store_color, store_rect)
    pygame.draw.rect(screen, editor_color, editor_rect)
    pygame.draw.rect(screen, stock_color, stock_rect)

    display_text(screen, "Store", BLACK, (store_rect.x + BUTTON_WIDTH/2 - 35, store_rect.y + BUTTON_HEIGHT/2 - 15))
    display_text(screen, "Editor", BLACK, (editor_rect.x + BUTTON_WIDTH/2 - 35, editor_rect.y + BUTTON_HEIGHT/2 - 15))
    display_text(screen, "Stock", BLACK, (stock_rect.x + BUTTON_WIDTH/2 - 35, stock_rect.y + BUTTON_HEIGHT/2 - 15))

    tablet = not interface_objects.exit_button.draw(mouse_pos, button_clicked)

    return store, tablet, editor, stock


def draw_bg(screen):
    pygame.draw.rect(screen, GRAY, (TABLET_OFFSET, TABLET_OFFSET, SCREEN_WIDTH - 2*TABLET_OFFSET, SCREEN_HEIGHT - 2*TABLET_OFFSET))