import pygame
import random

from App.Classes.box import Box
from App.Classes.player import Player

from App.Helpers.Constants.interface import *
from App.Helpers.customer_helper import random_customer
from App.Helpers.interface_tools import *
from App.Helpers.editor_helper import *
from App.Helpers.loading import *
from App.Interfaces.Tablet.store import *
from App.Interfaces.interface_objects import *
from App.Interfaces.Tablet.desktop import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)


interface_objects = InterfaceObjects(screen)
store_interface = load_store_interface(interface_objects)
interface_objects = load_interface_objects(interface_objects)
matrix = create_matrix(interface_objects.shelves)
player = Player(matrix)
customers = load_customers(matrix, store_interface.supermarket)

tablet = True
store = False
editor = False
editing_shelf = None 

elapsed_time = 0

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
            interface_objects.draw_temps()
            display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
        else:
            store, tablet, editor = tablet_interface(screen, button_clicked, mouse_pos, interface_objects)
            display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
            if editor: 
                shelves_editor_mode(interface_objects.shelves, editor)
        
    else:
        if editor:
            interface_objects.draw(mouse_pos, button_clicked)
            editing_shelf, interface_objects.shelves, editor, matrix = editor_helper(screen, button_clicked, mouse_pos, interface_objects, store_interface, editing_shelf, matrix)
            if not editor:
                for customer in customers:
                    customer.path_finder.update_matrix(matrix)
                player.path_finder.update_matrix(matrix)

        else:
            screen.fill(WHITE) ###################################################

            if elapsed_time == 0:
                start_time = pygame.time.get_ticks() 

            elapsed_time = ((pygame.time.get_ticks() - start_time) // 1000) + 1
            if elapsed_time >= 10:
                random_customer(customers, interface_objects)
                elapsed_time = 0
            
            if button_clicked:
                player.path_finder.create_path((mouse_pos[0], mouse_pos[1]), screen)
            player.path_finder.update(screen, (mouse_pos[0], mouse_pos[1]))

            interface_objects.draw(mouse_pos, button_clicked)

            for customer in customers:
                customer.path_finder.update(screen, (mouse_pos[0], mouse_pos[1]), interface_objects)
                customer.draw(screen)
 
            player.draw(screen)

            if keys[pygame.K_m]:
                tablet = True
            elif keys[pygame.K_n] and player.carrying_product == None:
                player.get_product(interface_objects.boxes)
            elif keys[pygame.K_b] and player.carrying_product != None:
                player.re_stock(interface_objects.shelves)
            elif keys[pygame.K_c]:
                player.cash_register(customers, interface_objects, screen)

            display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
