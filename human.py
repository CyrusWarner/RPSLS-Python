from player import Player


class Human(Player):
    def __init__(self):
        self.gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        self.chosen_gesture = " "
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = input("Please enter player ones name.")
        print(self.name)

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gesture_list:
            print(each)
            gesture_index += 1

    def choose_player_gesture(self):
        gesture_input = input("Choose your gesture!")
        for gesture in self.gesture_list:
            if gesture_input.lower() == gesture.lower():
                print(f"You chose {gesture}!\n")
                self.chosen_gesture = gesture

