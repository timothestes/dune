import uuid

from src.game.pieces.resources.manager import ResourceManager


class Player:
    def __init__(self, color: str, player_id: int = None):
        self.player_id = player_id or uuid.uuid4()
        self.hand = []
        self.points = 0
        self.color = color
        self.resources = self.get_starting_resources()

    def get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(self.color, **starting_resources)


if __name__ == "__main__":
    player = Player("Yellow", 1)
    print(player)
    print(player.resources)
