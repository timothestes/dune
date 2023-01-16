from src.game.pieces.agents.agent import Agent


class Mentat(Agent):
    def __init__(self, color: str):
        super().__init__()
        self.color = color
        self.name = "mentat"
