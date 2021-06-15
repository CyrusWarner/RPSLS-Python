from human import Human
from ai import AI
import random


class Battle:
    def __init__(self):
        self.human = Human()
        self.ai = AI()

    def run_game(self):
        self.welcome()

        self.battle()

        self.winner()

    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spook!")

    def battle(self):
        self.ai_turn()
        self.human_turn()

    def ai_turn(self):
        self.show_gesture_options()
        random_gesture = random.randint(0, len(self.ai.ai_gesture_list)-1)
        print(self.ai.ai_gesture_list[random_gesture])

    def human_turn(self):
        self.show_gesture_options()
        gesture_input = input("Choose your gesture!")
        for gesture in self.human.gesture_list:
            if gesture_input == gesture:
                print(f"{gesture_input}")

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.human.gesture_list:
            print(f"Your gesture option is {each}!")
            gesture_index += 1
        print("Please type in your gesture!")

    def winner(self):
        print("The winner of Rock Paper Scissors Lizard Spook is !")
        pass


