from human import Human
from ai import AI


class Battle:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.welcome()

        self.choose_game_mode()

        self.player_one_gesture()

        self.player_two_ai_gesture()

        self.game()

        self.winner()

    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spook!\n")
        print("You have the choice between Rock, Paper, Scissors, Lizard or Spook! After choosing the gesture you will either go against an ai or another player!\n")
        # determine winner of round

    def choose_game_mode(self):
        print("How many players? Max players is two")
        user_response = input()
        if user_response == 2:
            self.player_two = Human()
        else:
            self.player_two = AI()

    def player_one_gesture(self):
        self.player_one.show_gesture_options()
        self.player_one.choose_player_gesture()

    def player_two_ai_gesture(self):
        self.player_two.ai_choose_gesture()

    def game(self):
        if self.player_one.chosen_gesture.lower() == self.player_two.ai_chosen_gesture.lower():
            print("Tie!")
        if (self.player_one.chosen_gesture.lower() == "rock") & (self.player_two.ai_chosen_gesture.lower() == "scissors" or self.player_two.ai_chosen_gesture.lower() == "lizard"):
            print(f"{self.player_one.name} crushes {self.player_two.ai_chosen_gesture}")
            self.player_one.score += 1

    def winner(self):
        print("The winner of Rock Paper Scissors Lizard Spook is !")
        pass


