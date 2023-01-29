from numpy import random
from typing import List
from src.game.cards.card import Card


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)
