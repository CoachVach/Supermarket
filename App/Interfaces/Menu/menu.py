


from App.Helpers.Constants.interface import *
from App.Interfaces.Buttons.Menu.load_button import LoadButton
from App.Interfaces.Buttons.Menu.new_game import NewGameButton
from App.Interfaces.Buttons.Menu.save_button import SaveButton
from App.Interfaces.Buttons.Menu.settings_button import SettingsButton


class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.display = True

        self.new_game = NewGameButton(screen)
        self.save = SaveButton(screen)
        self.load = LoadButton(screen)
        self.settings = SettingsButton(screen)

    def draw(self, mouse_pos, button_clicked):
        tablet = False

        self.screen.fill(GRAY)

        new_game = self.new_game.draw(mouse_pos, button_clicked)
        save = self.save.draw(mouse_pos, button_clicked)
        load = self.load.draw(mouse_pos, button_clicked)
        settings = self.settings.draw(mouse_pos, button_clicked)
        
        if new_game: 
            self.display = False
            tablet = True
        elif save:
            pass
        elif load:
            pass
        elif settings:
            pass
        
        return tablet, new_game, save