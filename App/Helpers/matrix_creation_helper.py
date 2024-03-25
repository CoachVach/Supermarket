from App.Helpers.Constants.interface import *
from App.Helpers.Constants.logic import SHELF

def create_matrix(shelves):
    matrix_width = SCREEN_WIDTH
    matrix_height = SCREEN_HEIGHT

    cell_size = GRID_CELL_SIZE

    rows = matrix_width//cell_size
    columns = matrix_height//cell_size

    matrix = [[1 for _ in range(rows)] for _ in range(columns)]

    for shelf in shelves:
        for cell in shelf.interface.cells:
            matrix[cell[1]][cell[0]] = SHELF

    return matrix
