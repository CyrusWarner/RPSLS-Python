from human import Human
from ai import AI


class Battle:
    def __init__(self):
        pass

    def ai_turn(self):
        pass

    def human_turn(self):
        name_input = input("Please enter your name")
        Human(name_input)

    def winner(self):
        print("The winner of Rock Paper Scissors Lizard Spook is !")
        pass


