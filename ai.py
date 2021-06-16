from player import Player
import random


class AI(Player):
    def __init__(self):
        self.ai_gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        self.chosen_gesture = " "
        super().__init__()
        self.set_ai_name()

    def set_ai_name(self):
        self.name = "terminator"

    def choose_player_gesture(self):
        random_gesture = random.randint(0, len(self.ai_gesture_list) - 1)
        ai_gesture = self.ai_gesture_list[random_gesture]
        self.chosen_gesture = ai_gesture
