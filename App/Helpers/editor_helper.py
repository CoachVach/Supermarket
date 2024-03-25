import pygame

from App.Helpers.matrix_creation_helper import create_matrix

from ..Helpers.Constants.interface import *
from ..Classes.shelf import *

def editor_helper(screen, button_clicked, mouse_pos, interface_objects, store_interface, editing_shelf, matrix):

    shelves = interface_objects.shelves
    editor = True

    if editing_shelf == None:

        if interface_objects.exit_button.draw(mouse_pos, button_clicked):
            shelves_editor_mode(shelves, False)
            matrix = create_matrix(shelves)
            return editing_shelf, shelves, False, matrix

        if interface_objects.add_shelf_button.draw(mouse_pos, button_clicked):
            shelf = Shelf()
            if store_interface.supermarket.can_buy(shelf):
                new_shelf = shelf
                new_shelf.editor_mode(True)
                shelves.append(new_shelf)
                editing_shelf = new_shelf.interface
                editing_shelf.editing = True

                store_interface.supermarket.money -= new_shelf.cost()

        else:
            if button_clicked:
                for shelf in shelves:
                    shelf_interface = shelf.interface

                    if shelf_interface.rect().collidepoint(mouse_pos):
                        editing_shelf = shelf_interface
                        shelf_interface.editing = True
        
    else: 
        x, y = mouse_pos

        editing_shelf.update_position(x, y)

        editing_rect = editing_shelf.rect()

        collision = check_collisions(shelves, editing_shelf, editing_rect, screen)

        if button_clicked:
            if not collision:
                editing_shelf.editing = False
                editing_shelf = None

    return editing_shelf, shelves, editor, matrix

def check_collisions(shelves, editing_shelf, editing_rect, screen):
    collision = False
    for shelf in shelves:
        shelf_interface = shelf.interface
        if shelf_interface != editing_shelf:

            if shelf_interface.rect().colliderect(editing_rect):
                
                collision = True
                show_overlap(screen, editing_rect, shelf_interface.rect())

    return collision

def shelves_editor_mode(shelfs, editor):
    for shelf in shelfs:
        shelf.editor_mode(editor)

def show_overlap(screen, rect1, rect2):
    overlap_rect = rect1.clip(rect2)
    pygame.draw.rect(screen, BLUE, overlap_rect)