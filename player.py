class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.chosen_gesture = ""
        self.gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]

    def choose_player_gesture(self):
        gesture_input = input(f"\n{self.name} Choose your gesture!")
        for gesture in self.gesture_list:
            if gesture_input.lower() == gesture.lower():
                self.chosen_gesture = gesture
                return
        else:
            print("invalid input\n")
            self.choose_player_gesture()

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gesture_list:
            print(each)
            gesture_index += 1
