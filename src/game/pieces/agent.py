from src.game.pieces.piece import Piece

class Agent(Piece):
    def __init__(self, color: str):
        super().__init__()
        self.color = color
        self.name = "agent"
        self.activated = False
        self.current_position = None

    def is_activated(self):
        return self.activated

    def recall(self):
        self.activated = False
        self.current_position = None
