from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("Please enter your first name.")
        print(self.name)

    def player_gesture_options(self):
        rock = "Rock"
        scissors = "Scissors"
        paper = "Paper"
        lizard = "Lizard"
        spock = "Spock"
