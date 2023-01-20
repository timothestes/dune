from src.game.board.locations.location import Location
from dataclasses import dataclass, field


@dataclass
class Garrison(Location):
    color: str
    name: str = "garrison"
    agent_icon: str = "garrison"
    resources: dict = field(default_factory=dict)
    n_troops_in_garrison: int = 0
    n_troops_in_battle: int = 0

    @property
    def n_troops_in_supply(self):
        """Can be between 12 and 0."""
        return 12 - (self.n_troops_in_garrison + self.n_troops_in_battle)

    def add_troop_to_garrison(self) -> None:
        if self.n_troops_in_supply == 0:
            raise RuntimeError(
                f"No troops in {self.color} supply to deploy to garrison!"
            )
        self.n_troops_in_garrison += 1

    def remove_troop_from_garrison(self) -> None:
        if self.n_troops_in_garrison == 0:
            raise RuntimeError(
                f"No troops in {self.color} garrison to recall from battle!"
            )
        self.n_troops_in_garrison -= 1

    def add_troop_to_battle(self) -> None:
        if self.n_troops_in_garrison == 0:
            raise RuntimeError(
                f"No troops in {self.color} garrison to deploy to battle!"
            )
        self.n_troops_in_garrison -= 1
        self.n_troops_in_battle += 1

    def remove_troop_from_battle(self) -> None:
        if self.n_troops_in_battle == 0:
            raise RuntimeError(
                f"No troops in {self.color} garrison to recall from battle!"
            )
        self.n_troops_in_battle -= 1

    def remove_all_troops_from_battle(self) -> None:
        self.n_troops_in_garrison += self.n_troops_in_battle
        self.n_troops_in_battle = 0

    def __str__(self) -> str:
        return (
            f"{self.n_troops_in_garrison} troops in garrison, "
            f"{self.n_troops_in_battle} troops in battle, "
            f"{self.n_troops_in_supply} troops in supply."
        )
