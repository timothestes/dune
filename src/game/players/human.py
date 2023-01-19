from src.game.players.player import Player
from src.game.pieces.resources.manager import ResourceManager


class HumanPlayer(Player):
    def __init__(self, color: str, player_id: int = None):
        super().__init__(color, player_id)
        self.player_type = "human"

    def _get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(self.color, **starting_resources)