import pygame
import random

from App.Classes.box import Box
from App.Classes.player import Player

from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import *
from App.Helpers.editor_helper import *
from App.Helpers.loading import *
from App.Interfaces.Tablet.store import *
from App.Interfaces.interface_objects import *
from App.Interfaces.Tablet.desktop import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

player = Player()
interface_objects = InterfaceObjects(screen)
store_interface = load_store_interface(interface_objects)
interface_objects = load_interface_objects(interface_objects)

tablet = True
store = False
editor = False
editing_shelf = None

running = True
while running:
    screen.fill(WHITE) ###################################################
    button_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                button_clicked = True

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    if tablet:
        if store:
            store = store_interface.show(screen, button_clicked, mouse_pos, interface_objects)
            display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
            display_text(screen, f"${store_interface.supermarket}", BLACK, (20,70))
        else:
            store, tablet, editor = tablet_interface(screen, button_clicked, mouse_pos, interface_objects)
            display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
            if editor: 
                shelves_editor_mode(interface_objects.shelves)
        
    else:
        if editor:
            interface_objects.draw(mouse_pos, button_clicked)
            editing_shelf, interface_objects.shelves, editor = editor_helper(screen, button_clicked, mouse_pos, interface_objects, store_interface, editing_shelf)

        else:
            player.move(interface_objects.shelves)

            screen.fill(WHITE) ###################################################

            interface_objects.draw(mouse_pos, button_clicked)
 
            player.draw(screen)

            if keys[pygame.K_m]:
                tablet = True
            elif keys[pygame.K_n] and player.carrying_product == None:
                player.get_product(interface_objects.boxes)
            elif keys[pygame.K_b] and player.carrying_product != None:
                player.re_stock(interface_objects.shelves)

            display_text(screen, f"${store_interface.supermarket.money}", WHITE, (20,20))

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
