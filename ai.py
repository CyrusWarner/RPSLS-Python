from player import Player
import random


class AI(Player):
    def __init__(self):
        self.chosen_gesture = " "
        super().__init__()
        self.set_ai_name()

    def set_ai_name(self):
        self.name = "terminator"

    def choose_player_gesture(self):
        random_gesture = random.randint(0, len(self.gesture_list) - 1)
        ai_gesture = self.gesture_list[random_gesture]
        self.chosen_gesture = ai_gesture
