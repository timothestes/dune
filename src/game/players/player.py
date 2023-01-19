import uuid

from src.game.pieces.resources.manager import ResourceManager
from src.game.players.influence_manager import InfluenceManager
from src.game.board.locations.garrison import Garrison
from src.game.leaders.leader import Leader


class Player:
    def __init__(
        self,
        color: str,
        leader: Leader,
        player_id: int = None,
    ):
        self.player_id = player_id
        if player_id is None:
            self.player_id = uuid.uuid4()
        self.leader = leader
        self.hand = []
        self.points = 0
        self.color = color
        self.resources = self._get_starting_resources()
        self.influence = self._get_starting_influence()
        self.garrison = self._get_starting_garrison()

    def _get_starting_garrison(self) -> Garrison:
        return Garrison(color=self.color, n_troops_in_garrison=3)

    def _get_starting_resources(self):
        starting_resources = {"water": 1, "spice": 0, "solari": 0}
        return ResourceManager(**starting_resources)

    def _get_starting_influence(self):
        starting_influence = {
            "emperor": 0,
            "spacing_guild": 0,
            "bene_gesserit": 0,
            "fremen": 0,
        }
        return InfluenceManager(**starting_influence)

    def __str__(self):
        return (
            f"Player {self.player_id} ({self.color}): \n  "
            f"Resources: {self.resources} \n  "
            f"Influence: {self.influence} \n  "
            f"Points: {self.points} \n  "
            f"Garrison: {self.garrison} \n  "
        )
