import pygame

from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import display_text


class DayReport:
    def __init__(self, sells, buys):
        self.sells = sells
        self.buys = buys

    def draw(self, screen, space):
            pygame.draw.rect(screen, DARK_GRAY, (TABLET_OFFSET, TABLET_OFFSET, SCREEN_WIDTH - 2*TABLET_OFFSET, SCREEN_HEIGHT - 2*TABLET_OFFSET))
            
            profit = self.sells - self.buys

            display_text(screen, f"Day Report", WHITE, (300, 150))
            display_text(screen, f"Sells: ${self.sells}", WHITE, (200, 200))
            display_text(screen, f"Buys: ${self.buys}", WHITE, (200, 240))
            color = GREEN if profit >= 0 else RED
            display_text(screen, f"Profit: ${profit}", color, (200, 280))

            display_text(screen, "SPACE TO START A NEW DAY", WHITE, (200, 400))

            if not space:
                return True
            else:
                self.buys = 0
                self.sells = 0

                return False