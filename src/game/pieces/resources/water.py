from src.game.pieces.resources.resource import Resource


class Water(Resource):
    def __init__(self):
        super().__init__()
        self.name = "water"
