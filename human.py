from player import Player


class Human(Player):
    def __init__(self):
        self.gesture_list = []
        super().__init__()
        self.player_gesture_options()

    def set_name(self):
        self.name = input("Please enter your first name.")
        print(self.name)

    def player_gesture_options(self):
        rock = "Rock"
        scissors = "Scissors"
        paper = "Paper"
        lizard = "Lizard"
        spock = "Spock"
        self.gesture_list.append(rock)
        self.gesture_list.append(scissors)
        self.gesture_list.append(paper)
        self.gesture_list.append(lizard)
        self.gesture_list.append(spock)

