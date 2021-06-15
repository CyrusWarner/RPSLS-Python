from player import Player
import random


class AI(Player):
    def __init__(self):
        self.ai_gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        super().__init__()
        self.ai_choose_gesture()

    def set_ai_name(self):
        self.name = "terminator"

    def ai_choose_gesture(self):
        random_gesture = random.randint(0, len(self.ai_gesture_list) - 1)
        ai_gesture = self.ai_gesture_list[random_gesture]
        print(f"Your oppenent chose {ai_gesture}!")
