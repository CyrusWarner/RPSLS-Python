class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.chosen_gesture = ""
        self.gestures = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]

    def choose_player_gesture(self):
        gesture_input = input("Choose your gesture!")
        for gesture in self.gestures:
            if gesture_input.lower() == gesture.lower():
                print(f"{gesture_input}")
