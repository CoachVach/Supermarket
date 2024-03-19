import pygame
from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import *
from ..Buttons.exit_button import *

def tablet_interface(screen, button_clicked, mouse_pos, interface_objects):
    store = False
    tablet = True
    editor = False

    draw_bg(screen)
    store_rect = pygame.Rect(BUTTON_OFFSET + TABLET_OFFSET, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    editor_rect = pygame.Rect(BUTTON_OFFSET + 2*TABLET_OFFSET + BUTTON_WIDTH, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

    store_color = WHITE
    editor_color = WHITE

    if store_rect.collidepoint(mouse_pos):
        if button_clicked:
            store = True
        store_color = RED
    elif editor_rect.collidepoint(mouse_pos):
        if button_clicked:
            editor = True
            tablet = False
            return store, tablet, editor
        editor_color = RED

    pygame.draw.rect(screen, store_color, store_rect)
    pygame.draw.rect(screen, editor_color, editor_rect)

    display_text(screen, "Store", BLACK, (store_rect.x + BUTTON_WIDTH/2 - 35, store_rect.y + BUTTON_HEIGHT/2 - 15))
    display_text(screen, "Editor", BLACK, (editor_rect.x + BUTTON_WIDTH/2 - 35, editor_rect.y + BUTTON_HEIGHT/2 - 15))

    tablet = not interface_objects.exit_button.draw(mouse_pos, button_clicked)

    return store, tablet, editor


def draw_bg(screen):
    pygame.draw.rect(screen, GRAY, (TABLET_OFFSET, TABLET_OFFSET, SCREEN_WIDTH - 2*TABLET_OFFSET, SCREEN_HEIGHT - 2*TABLET_OFFSET))