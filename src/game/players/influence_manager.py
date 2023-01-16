class InfluenceManager:
    def __init__(
        self,
        emperor: int = 0,
        spacing_guild: int = 0,
        bene_gesserit: int = 0,
        fremen: int = 0,
    ):
        self.max_influence = 6
        self.emperor = emperor
        self.spacing_guild = spacing_guild
        self.bene_gesserit = bene_gesserit
        self.fremen = fremen

    def add(self, influence_type: str, amount: int):
        """Add influence to the given influence type"""
        if self._should_add(influence_type):
            self._increment(influence_type, amount)
        else:
            raise ValueError("Invalid influence type or too much influence")

    def remove(self, influence_type: str, amount: int):
        if self._should_remove(influence_type):
            self._decrement(influence_type, amount)
        else:
            raise ValueError("Invalid influence type or not enough influence")

    def _should_add(self, influence_type: str) -> bool:
        """Should we add an influence to the given influence type?"""
        if hasattr(self, influence_type):
            class_influence = getattr(self, influence_type)
            return class_influence < self.max_influence

    def _should_remove(self, influence_type: str) -> bool:
        """Should we remove an influence from the given influence type?"""
        if hasattr(self, influence_type):
            class_influence = getattr(self, influence_type)
            return class_influence > 0

    def _increment(self, resource_name: str, amount: int) -> None:
        setattr(self, resource_name, getattr(self, resource_name) + amount)

    def _decrement(self, resource_name: str, amount: int) -> None:
        setattr(self, resource_name, getattr(self, resource_name) - amount)

    def __str__(self) -> str:
        return (
            f"Emperor: {self.emperor}, Spacing Guild: {self.spacing_guild}, "
            f"Bene Gesserit: {self.bene_gesserit}, Fremen: {self.fremen}"
        )
