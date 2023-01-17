from src.game.cards.card import Card


class HouseHagalCard(Card):
    def __init__(
        self,
        name: str,
        name_friendly: str,
        location: str,
        combat_value: int,
        resources: dict,
        quantity_in_deck: bool,
    ):
        self.name = name
        self.name_friendly = name_friendly
        self.location = location
        self.combat_value = combat_value
        self.resources = resources
        self.quantity_in_deck = quantity_in_deck
