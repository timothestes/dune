from src.game.board.locations.location import Location
from dataclasses import dataclass, field

def get_resources():
    return {"spice": 100}

@dataclass
class Arrakis(Location):
    name: str = "arrakis"
    location_type: str = "planet"
    resources: dict = field(default_factory=get_resources)

    def location_effects(self):
        print(f"Welcome to {self.name}! We have {self.resources}!")

if __name__ == "__main__":
    location = Arrakis()
    location.location_effects()
