import pygame, sys

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

from App.Helpers.Constants.interface import GRID_CELL_SIZE, RED

class Pathfinder:
	def __init__(self, matrix, customer):

		# setup
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)

		# pathfinding
		self.path = []

		self.customer = customer

	def empty_path(self):
		self.path = []

	def update_matrix(self, matrix):
		self.grid = Grid(matrix = matrix)

	def draw_active_cell(self, screen, point):
		end_x,end_y = point
		end_x //= GRID_CELL_SIZE
		end_y //= GRID_CELL_SIZE
		current_cell_value = self.matrix[end_y][end_x]
		if current_cell_value == 1:
			rect = pygame.Rect((end_x * GRID_CELL_SIZE,end_y * GRID_CELL_SIZE),(GRID_CELL_SIZE,GRID_CELL_SIZE))
			pygame.draw.rect(screen, RED, rect)

	def create_path(self, point, screen):

		start_x, start_y = self.customer.get_coord()
		start = self.grid.node(start_x,start_y)

		end_x,end_y = point
		end_x //= GRID_CELL_SIZE
		end_y //= GRID_CELL_SIZE

		end = self.grid.node(end_x,end_y) 

		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
		self.path,_ = finder.find_path(start,end,self.grid)
		self.grid.cleanup()
		self.customer.set_path(self.path, screen)

	def draw_path(self, screen):
		if self.path:
			points = []
			for point in self.path:
				x = (point.x * GRID_CELL_SIZE) + GRID_CELL_SIZE//2
				y = (point.y * GRID_CELL_SIZE) + GRID_CELL_SIZE//2
				points.append((x,y))

			pygame.draw.lines(screen,'#4a4a4a',False,points,5)

	def update(self, screen, point):
		self.draw_active_cell(screen, point)
		self.draw_path(screen)

		self.customer.move()