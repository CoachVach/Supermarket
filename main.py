import pygame

from App.Classes.player import Player

from App.Classes.report import DayReport
from App.Helpers.Constants.interface import *
from App.Helpers.Loading.prev_game import load_db
from App.Helpers.Loading.saving import save_db
from App.Helpers.customer_helper import random_customer
from App.Helpers.interface_tools import *
from App.Helpers.editor_helper import *
from App.Helpers.Loading.new_game import *
from App.Interfaces.Menu.menu import Menu
from App.Interfaces.Tablet.store import *
from App.Interfaces.interface_objects import *
from App.Interfaces.Tablet.desktop import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

menu = Menu(screen)
tablet = False
store = False
stock = False
editor = False
reporting = False
space = False
editing_shelf = None 

elapsed_time = 0
open = False
opened_time = 0
displayed_time = 0

running = True
while running:
    screen.fill(WHITE) ###################################################
    button_clicked = False
    key_released = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                button_clicked = True
        elif event.type == pygame.KEYUP:
            key_released = True
        elif event.type == pygame.KEYDOWN:
            space = event.key == pygame.K_SPACE

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    if menu.display:
        tablet, new_game, save, load = menu.draw(mouse_pos, button_clicked)
        if tablet and new_game:
            interface_objects, store_interface, matrix, player, customers, stock_interface = load_new_game(screen)
        elif save:
            save_db(interface_objects, store_interface, customers, stock_interface)
        elif load:
            interface_objects, store_interface, matrix, player, customers, stock_interface = load_db(screen)
    else:
        if tablet:
            if store:
                store = store_interface.show(screen, button_clicked, mouse_pos, interface_objects)
                interface_objects.draw_temps()
                display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
            elif stock:
                stock = stock_interface.show(screen, button_clicked, mouse_pos)
                display_text(screen, f"${store_interface.supermarket.money}", BLACK, (20,20))
            else:
                store, tablet, editor, stock = tablet_interface(screen, button_clicked, mouse_pos, interface_objects)
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
                screen.fill(BLACK) ###################################################
                
                if button_clicked:
                    player.path_finder.create_path((mouse_pos[0], mouse_pos[1]), screen)
                player.path_finder.update(screen, (mouse_pos[0], mouse_pos[1]))

                interface_objects.draw(mouse_pos, button_clicked)

                for customer in customers:
                    customer.path_finder.update(screen, (mouse_pos[0], mouse_pos[1]), interface_objects)
                    customer.draw(screen)
    
                player.draw(screen)

                if open:
                    if elapsed_time == 0:
                        start_time = pygame.time.get_ticks() 

                    if opened_time == 0:
                        open_time = pygame.time.get_ticks() 

                    opened_time = ((pygame.time.get_ticks() - open_time) // 1000) + 1   
                    elapsed_time = ((pygame.time.get_ticks() - start_time) // 1000) + 1
                    if elapsed_time >= 10:
                        random_customer(customers, interface_objects)
                        elapsed_time = 0

                    hour = 8 + opened_time//6
                    minute = opened_time % 6
                    minute = f"{minute}0"

                    display_text(screen, f"{hour}:{minute}", WHITE, (SCREEN_WIDTH - 75, 0))

                    if opened_time == CLOSING_TIME:
                        reporting = True
                        report = DayReport(50, 30)
                        open = False
                        opened_time, elapsed_time = 0,0
                else:
                    if displayed_time == 0:
                        start_time = pygame.time.get_ticks() 

                    displayed_time = ((pygame.time.get_ticks() - start_time) // 1000) + 1
                    if (displayed_time % 2) == 0:
                        display_text(screen, "SPACE TO OPEN", WHITE, (300, 300))

                if reporting:
                    reporting = report.draw(screen, space and key_released)
                else:
                    if keys[pygame.K_m]: 
                        tablet = True
                    elif keys[pygame.K_n] and player.carrying_product == None:
                        player.get_product(interface_objects.boxes)
                    elif keys[pygame.K_b] and player.carrying_product != None:
                        player.re_stock(interface_objects.shelves)
                    elif keys[pygame.K_c]:
                        player.cash_register(customers, interface_objects, screen)
                    elif space and key_released and open == False:
                        open = True
                        spae = False
                    elif keys[pygame.K_ESCAPE]:
                        menu.display = True
                        store, tablet, editor = False, False, False

                money = "{:.2f}".format(store_interface.supermarket.money)

                display_text(screen, f"${money}", WHITE, (20,20))

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
