from src.game.players.player import Player
from src.game.pieces.resources.manager import ResourceManager


class HumanPlayer(Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_type = "human"

    def _get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(**starting_resources)
