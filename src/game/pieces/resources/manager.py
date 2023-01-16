from src.game.pieces.resources.resource import Resource


class ResourceManager:
    def __init__(
        self,
        water: int = 0,
        spice: int = 0,
        solari: int = 0,
        intruige: int = 0,
    ):
        self.water = water
        self.spice = spice
        self.solari = solari
        self.intruige = intruige

    def _should_add(self, resource_name: str) -> bool:
        """Should we add an resource to the given resource type?"""
        return hasattr(self, resource_name)

    def _increment(self, resource_name: str, amount: int) -> None:
        setattr(self, resource_name, getattr(self, resource_name) + amount)

    def _decrement(self, resource_name: str, amount: int) -> None:
        setattr(self, resource_name, getattr(self, resource_name) - amount)

    def _should_remove(self, resource_name: str) -> bool:
        """Should we remove an resource from the given resource type?"""
        return hasattr(self, resource_name) and getattr(self, resource_name) > 0

    def add(self, resource: Resource or str, amount: int):
        resource_name = resource.name if isinstance(resource, Resource) else resource
        if self._should_add(resource_name):
            self._increment(resource, amount)
        else:
            raise ValueError("Invalid resource")

    def remove(self, resource: Resource or str):
        resource_name = resource.name if isinstance(resource, Resource) else resource
        if self._should_remove(resource_name):
            self._decrement(resource)

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
