from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()

    def set_ai_name(self):
        self.name = "terminator"
