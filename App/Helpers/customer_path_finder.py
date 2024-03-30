from App.Helpers.path_finder import Pathfinder
from pathfinding.core.grid import Grid


class CustomerPathfinder(Pathfinder):

    def create_path_shelf(self, point, screen, interface_objects):

        previous_matrix = self.matrix
        self.matrix = self.normalized_matrix(point, interface_objects)
        self.grid = Grid(matrix = self.matrix)

        super().create_path(point, screen)

        self.matrix = previous_matrix
        self.grid = Grid(matrix = self.matrix)

    def update(self, screen, point, interface_objects):
        self.draw_path(screen)

        self.customer.move(screen, interface_objects)

    def normalized_matrix(self, point, interface_objects):
        shelf = interface_objects.get_shelf(point)

        matrix = self.matrix

        for cell in shelf.interface.cells:
            matrix[cell[1]][cell[0]] = 1

        return matrix

