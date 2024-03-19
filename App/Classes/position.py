import pygame

class Position:
    def __init__(self, x=0, y=0, width=5, height=5,):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    