from src.game.cards.card import Card


class CombatCard(Card):
    def __init__(
        self, name: str, name_friendly: str, conflict_level: str, rewards: dict
    ):
        self.name_friendly = name_friendly
        self.conflict_level = conflict_level
        self.rewards = rewards
        self.first_place: dict = self.rewards["first"]
        self.second_place: dict = self.rewards["second"]
        self.third_place: dict = self.rewards["third"]
        super().__init__(name)
