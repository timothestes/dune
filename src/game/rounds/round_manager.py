from src.game.players.player import Player
from typing import List
from src.game.board.board import Board
from src.game.cards.decks.combat import CombatDeck


class RoundManager:
    def __init__(
        self,
        board: Board,
        combat_deck: CombatDeck,
        first_player: Player,
        turn_order: List[Player],
    ):
        self.board = board
        self.combat_deck = combat_deck
        self.first_player = first_player
        self.turn_order = turn_order

    def start_new_round(self) -> None:
        # reveal a new conflict card
        self.current_combat = self.combat_deck.draw_card()
        print(self.current_combat.name_friendly)

        # each player draws a hand of five cards
        for player in self.turn_order:
            player.draw_new_hand()

    def take_player_turns(self) -> None:
        for player in self.turn_order:
            player.take_turn()

    def resolve_combat(self) -> None:
        """Determine the combat points for each player."""
        combat = {}
        for player in self.turn_order:
            player.play_combat_cards()
            combat[player] = player.get_combat_points()

        self._determine_prizes(combat)
        self._cleanup_combat()

    def _determine_prizes(self, combat: dict) -> None:
        """Determine the prizes for each player."""
        return "TODO"

    def _cleanup_combat(self) -> None:
        """Clean up the combat."""
        for player in self.turn_order:
            player.garrison.remove_all_troops_from_battle()

    def update_makers(self) -> None:
        self.board.update_makers()

    def recall_phase(self) -> None:
        for player in self.turn_order:
            # check for endgame
            if player.points >= 10:
                self.state = "ended"
                return

            # remove mentat agents
            for agent in player.agents:
                if agent.name == "mentat":
                    player.agents.remove(agent)
                else:
                    agent.recall()
