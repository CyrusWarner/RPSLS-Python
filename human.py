from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("Please enter your first name.")
        print(self.name)
