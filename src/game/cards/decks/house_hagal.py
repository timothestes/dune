from src.game.cards.decks.deck import Deck
import json
from typing import List
from src.game.cards.house_hagal import HouseHagalCard


class HagalDeck(Deck):
    def __init__(self):
        cards = self.get_cards()
        super().__init__(cards)

    def get_cards(self):
        with open("resources/dune_imperium.json") as f:
            data: dict = json.load(f)
            cards = data.get("house_hagal_cards")
            return self.load_cards(cards)

    def load_cards(self, cards: List[dict]) -> List[HouseHagalCard]:
        return [HouseHagalCard(**card) for card in cards]
