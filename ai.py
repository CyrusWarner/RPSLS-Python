from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()

    def set_ai_name(self):
        self.name = "terminator"

    def ai_gesture_options(self):
        rock = "Rock"
        scissors = "Scissors"
        paper = "Paper"
        lizard = "Lizard"
        spock = "Spock"
