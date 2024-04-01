import pygame
from App.Helpers.Constants.interface import *

pygame.init()

font = pygame.font.Font(None, FONT_SIZE)

def display_text(screen, text, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)


def display_custom_text(screen, text, font_size, color, position):
    custom_font = pygame.font.Font(None, font_size)
    rendered_text = custom_font.render(text, True, color)
    screen.blit(rendered_text, position)