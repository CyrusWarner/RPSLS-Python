from human import Human
from ai import AI


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
        

    def ai_turn(self):
        pass

    def human_turn(self):
       pass

    def winner(self):
        print("The winner of Rock Paper Scissors Lizard Spook is !")
        pass


