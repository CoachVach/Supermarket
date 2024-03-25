import pygame

from ...Helpers.Constants.interface import *
from ...Helpers.Constants.logic import *
from ...Classes.position import Position

class ShelfInterface():

    def __init__(self):
        self.position = Position(MAP_OFFSET, MAP_OFFSET, SHELF_WIDTH, SHELF_HEIGHT)
        self.color = DARK_GRAY
        self.color_editor = GRAY
        self.vertical = False
        self.editor = False
        self.editing = False
        self.cells = self.get_cells()

    def get_cells(self):
        position = self.position
        i = position.x // GRID_CELL_SIZE
        j = position.y // GRID_CELL_SIZE

        cells = [[i, j],[i+1, j],[i+2, j], [i+3, j]
                 ,[i, j+1],[i+1, j+1],[i+2, j+1], [i+3, j+1]]
        return cells

    def draw(self, screen, button_clicked, mouse_pos, product, amount):
        self.draw_shelf(screen, button_clicked, mouse_pos)

        for i in range(amount):
            position = Position(self.product_x(i), self.product_y(i), self.product_width(), self.product_height())
            product.draw(screen, position)

    def draw_shelf(self, screen, button_clicked, mouse_pos):
        color = self.color_editor if self.editor else self.color
        width = self.position.height if self.vertical else self.position.width 
        height = self.position.width if self.vertical else self.position.height 
        pygame.draw.rect(screen, color, (self.position.x, self.position.y, width, height))

    def update_position(self, x, y):
        self.position.x = x - (x % GRID_CELL_SIZE)
        self.position.y = y - (y % GRID_CELL_SIZE)

        self.cells = self.get_cells()

    def orientation(self, vertical):
        self.vertical = vertical

    def product_x(self, i):
        mod = i % 2 if self.vertical else i % 3

        return self.position.x + (mod * self.product_width())

    def product_y(self, i):
        mod = i // 2 if self.vertical else i // 3
            
        return self.position.y + (mod * self.product_height())
        
    def product_width(self):
        if self.vertical:
            return self.position.height / 2
        else:
            return self.position.width / 3
        
    def product_height(self):
        if self.vertical:
            return self.position.width / 3
        else:
            return self.position.height / 2

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.position.width, self.position.height) 