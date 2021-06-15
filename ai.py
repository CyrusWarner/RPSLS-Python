from player import Player


class AI(Player):
    def __init__(self):
        self.ai_gesture_list = []
        super().__init__()
        self.ai_gesture_options()

    def set_ai_name(self):
        self.name = "terminator"

    def ai_gesture_options(self):
        rock = "Rock"
        scissors = "Scissors"
        paper = "Paper"
        lizard = "Lizard"
        spock = "Spock"
        self.ai_gesture_list.append(rock)
        self.ai_gesture_list.append(scissors)
        self.ai_gesture_list.append(paper)
        self.ai_gesture_list.append(lizard)
        self.ai_gesture_list.append(spock)

