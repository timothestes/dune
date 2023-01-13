from src.game.pieces.piece import Piece


class Troop(Piece):
    def __init__(self, color: str):
        super().__init__()
        self.color = color
        self.name = "troop"
        self.combat_value = 2
