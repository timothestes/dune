import json
from typing import List
import numpy
import random
from src.game.cards.combat import CombatCard
from src.game.cards.decks.deck import Deck


class CombatDeck(Deck):
    def __init__(self, board_type: str):
        cards = self.get_cards(board_type)
        self.combat_one_cards = self.get_combat_one_deck(cards)
        self.combat_two_cards = self.get_combat_two_deck(cards)
        self.combat_three_cards = self.get_combat_three_deck(cards)
        self.combat_level = 1
        super().__init__(cards)

    def get_cards(self, board_type: str) -> List[CombatCard]:
        output = []
        with open("resources/dune_imperium.json") as f:
            output.extend(self._load_cards_from_f(f))
        if board_type == "rise_of_ix":
            with open("resources/rise_of_ix.json") as f:
                output.extend(self._load_cards_from_f(f))
        return output

    def _load_cards_from_f(self, f):
        data: dict = json.load(f)
        cards = data["combat_cards"]
        return self.load_cards(cards)

    def load_cards(self, cards: List[dict]) -> List[CombatCard]:
        return [CombatCard(**card) for card in cards]

    def get_combat_one_deck(self, cards: List[CombatCard]) -> List[CombatCard]:

        return random.sample(
            [card for card in cards if card.conflict_level == 1],
            1,
        )

    def get_combat_two_deck(self, cards: List[CombatCard]) -> List[CombatCard]:
        return random.sample(
            [card for card in cards if card.conflict_level == 2],
            5,
        )

    def get_combat_three_deck(
        self, cards: List[CombatCard]
    ) -> List[CombatCard]:
        return random.sample(
            [card for card in cards if card.conflict_level == 3],
            3,
        )

    def draw_card(self) -> CombatCard:
        if self.combat_level == 1:
            card_to_return = self.combat_one_cards.pop()
            if not self.combat_one_cards:
                self.combat_level = 2
        elif self.combat_level == 2:
            card_to_return = self.combat_two_cards.pop()
            if not self.combat_two_cards:
                self.combat_level = 3
        elif self.combat_level == 3:
            if not self.combat_three_cards:
                raise RuntimeError("No more cards in combat deck")
            card_to_return = self.combat_three_cards.pop()

        return card_to_return


if __name__ == "__main__":
    deck = CombatDeck()
    print(deck.cards)
