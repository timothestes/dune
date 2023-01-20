from src.game.players.player import Player
from src.game.pieces.resources.manager import ResourceManager


class HouseHagalPlayer(Player):
    def __init__(self, turns_until_swordmaster: int, **kwargs):
        super().__init__(**kwargs)
        self.turns_until_swordmaster = turns_until_swordmaster
        self.player_type = "house_hagal"

    def _get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(**starting_resources)
