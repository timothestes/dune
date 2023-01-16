from src.game.pieces.resources.resource import Resource


class ResourceManager:
    def __init__(
        self,
        color: str,
        water: int = 0,
        spice: int = 0,
        solari: int = 0,
        intruige: int = 0,
    ):
        self.color = color
        self.water = water
        self.spice = spice
        self.solari = solari
        self.intruige = intruige

    def is_water(self, resource: Resource or str):
        return resource.name == "water" or resource == "water"

    def is_spice(self, resource: Resource or str):
        return resource.name == "spice" or resource == "spice"

    def is_solari(self, resource: Resource or str):
        return resource.name == "solari" or resource == "solari"

    def is_intruige(self, resource: Resource or str):
        return resource.name == "intruige" or resource == "intruige"

    def add_resource(self, resource: Resource or str):
        if self.is_water(resource):
            self.water += 1
        elif self.is_spice(resource):
            self.spice += 1
        elif self.is_solari(resource):
            self.solari += 1
        elif self.is_intruige(resource):
            self.intruige += 1
        else:
            raise ValueError("Invalid resource")

    def remove_resource(self, resource: Resource or str):
        if self.is_water(resource) and self.water > 0:
            self.water -= 1
        elif self.is_spice(resource) and self.spice > 0:
            self.spice -= 1
        elif self.is_solari(resource) and self.solari > 0:
            self.solari -= 1
        elif self.is_intruige(resource) and self.intruige > 0:
            self.intruige -= 1
        else:
            raise ValueError("Invalid resource or not enough resources")

    def __str__(self):
        return (
            f"Water: {self.water}, Spice: {self.spice}, "
            f"Solari: {self.solari}, Intruige: {self.intruige}"
        )

    def __dict__(self):
        return {
            "water": self.water,
            "spice": self.spice,
            "solari": self.solari,
            "intruige": self.intruige,
        }
