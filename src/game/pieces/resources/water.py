from src.game.pieces.piece import Piece


class Water(Piece):
    def __init__(self):
        super().__init__()
        self.name = "water"
