from App.Interfaces.Map.cash_register import CashRegisterInterface


class CashRegister:
    def __init__(self):
        self.interface = CashRegisterInterface()
        self.sound = "Sounds/bar_code.mp3"

    def draw(self, screen):
        self.interface.draw(screen)
