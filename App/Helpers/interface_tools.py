import pygame
from App.Helpers.Constants.interface import *

pygame.init()

font = pygame.font.Font(None, FONT_SIZE)

def display_text(screen, text, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)