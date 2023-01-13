from src.game.pieces.agents.agent import Agent


class Mentat(Agent):
    def __init__(self, color: str):
        super().__init__()
        self.color = color
        self.name = "mentat"
        self.activated = False

    def is_activated(self):
        return self.activated

    def activate(self):
        self.activated = True

    def recall(self):
        self.activated = False
