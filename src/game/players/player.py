import uuid

from src.game.pieces.resources.manager import ResourceManager
from src.game.players.influence_manager import InfluenceManager


class Player:
    def __init__(self, color: str, player_id: int = None):
        self.player_id = player_id or uuid.uuid4()
        self.hand = []
        self.points = 0
        self.color = color
        self.resources = self.get_starting_resources()
        self.influence = self.get_starting_influence()

    def get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(self.color, **starting_resources)

    def get_starting_influence(self):
        starting_influence = {
            "emperor": 0,
            "spacing_guild": 0,
            "bene_gesserit": 0,
            "fremen": 0,
        }
        return InfluenceManager(**starting_influence)


if __name__ == "__main__":
    player = Player("Yellow", 1)
    print(player)
    print(player.resources)
    print(player.influence.fremen)
