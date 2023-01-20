from src.game.pieces.agents.agent import Agent


class Swordmaster(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "swordmaster"
