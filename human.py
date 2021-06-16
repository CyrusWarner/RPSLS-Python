from player import Player


class Human(Player):
    def __init__(self):
        self.chosen_gesture = " "
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = input("\nPlease enter player name.\n")
