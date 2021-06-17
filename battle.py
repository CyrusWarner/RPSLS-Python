from human import Human
from ai import AI


class Battle:
    def __init__(self):

        self.player_one = None
        self.player_two = None

    def run_game(self):

        self.welcome()

        self.choose_game_mode()

        self.player_one_gesture()

        self.player_two_gesture()

        self.game()

        self.winner()

        self.play_again()

    def welcome(self):

        print("\nWelcome to Rock Paper Scissors Lizard Spook!\n")
        print("You have the choice between Rock, Paper, Scissors, Lizard or Spook! After choosing the gesture you will either go against an ai or another player!\n")
        # determine winner of round

    def choose_game_mode(self):

        print("How many players? Max players is two")
        user_response = int(input())
        if user_response == 2:
            self.player_one = Human()
            self.player_two = Human()
        else:
            self.player_one = Human()
            self.player_two = AI()

    def player_one_gesture(self):

        self.player_one.show_gesture_options()
        self.player_one.choose_player_gesture()

    def player_two_gesture(self):

        self.player_two.choose_player_gesture()

    def game(self):

        while self.player_one.score < 3 and self.player_two.score < 3:
            if self.player_one.score == 3:
                self.winner()

            if self.player_two.score == 3:
                self.winner()

            if self.player_one.chosen_gesture.lower() == self.player_two.chosen_gesture.lower():
                print("Tie!")

            elif (self.player_one.chosen_gesture.lower() == "rock") & (self.player_two.chosen_gesture.lower() == "scissors" or self.player_two.chosen_gesture.lower() == "lizard"):
                print(f"{self.player_one.chosen_gesture} crushes {self.player_two.chosen_gesture}")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "scissors") & (self.player_two.chosen_gesture.lower() == "paper"):
                print("Scissors cuts Paper")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "scissors") & (self.player_two.chosen_gesture.lower() == "lizard"):
                print("Scissors decapitates Lizard")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "paper") & (self.player_two.chosen_gesture.lower() == "rock"):
                print("Paper covers Rock")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "paper") & (self.player_two.chosen_gesture.lower() == "spock"):
                print("Paper disproves Spock")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "lizard") & (self.player_two.chosen_gesture.lower() == "spock"):
                print("Lizard poisons Spock")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "lizard") & (self.player_two.chosen_gesture.lower() == "paper"):
                print("Lizard eats Paper")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "spock") & (self.player_two.chosen_gesture.lower() == "scissors"):
                print("Spock smashes scissors")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            elif (self.player_one.chosen_gesture.lower() == "spock") & (self.player_two.chosen_gesture.lower() == "rock"):
                print("Spock vaporizes rock")
                print(f"{self.player_one.name} won the round!\n")
                self.player_one.score += 1

            # Player two if statements start on line 95
            elif (self.player_two.chosen_gesture.lower() == "rock") & (self.player_one.chosen_gesture.lower() == "scissors" or self.player_one.chosen_gesture.lower() == "lizard"):
                print(f"{self.player_two.chosen_gesture} crushes {self.player_one.chosen_gesture}")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "scissors") & (self.player_one.chosen_gesture.lower() == "paper"):
                print("Scissors cuts Paper")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "scissors") & (self.player_one.chosen_gesture.lower() == "lizard"):
                print("Scissors decapitates Lizard")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "paper") & (self.player_one.chosen_gesture.lower() == "rock"):
                print("Paper covers Rock")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "paper") & (self.player_one.chosen_gesture.lower() == "spock"):
                print("Paper disproves Spock")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "lizard") & (self.player_one.chosen_gesture.lower() == "spock"):
                print("Lizard poisons Spock")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "lizard") & (self.player_one.chosen_gesture.lower() == "paper"):
                print("Lizard eats Paper")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "spock") & (self.player_one.chosen_gesture.lower() == "scissors"):
                print("Spock smashes scissors")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            elif (self.player_two.chosen_gesture.lower() == "spock") & (self.player_one.chosen_gesture.lower() == "rock"):
                print("Spock vaporizes rock")
                print(f"{self.player_two.name} won the round!\n")
                self.player_two.score += 1

            if self.player_one.score < 3 and self.player_two.score < 3:
                self.player_one_gesture()
                self.player_two_gesture()

    def winner(self):

        if self.player_one.score == 3:
            print(f"The winner is {self.player_one.name}!")

        if self.player_two.score == 3:
            print(f"The winner is {self.player_two.name}!")

    def play_again(self):
        again = input("Would you like to play again? Please type in yes or no.")
        if again.lower() == "yes":
            self.run_game()
        elif again.lower() == "no":
            print("I hope you enjoyed!")
        elif again.lower != "yes" and "no":
            print("Invalid input")
            self.play_again()


