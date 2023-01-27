import random
from typing import List
import json

from src.game.board.board import Board
from src.game.leaders.leader import Leader
from src.game.players.house_hagal import HouseHagalPlayer
from src.game.players.human import HumanPlayer
from src.game.players.player import Player
from src.game.rounds.round_manager import RoundManager
from src.game.cards.decks.combat import CombatDeck


class Game:
    """
    A class representing a game.
    """

    def __init__(
        self,
        n_human_players: int,
        n_house_hagal_players: int = 0,
        difficulty: str = "novice",
        board_type: str = "base",
    ):
        """
        Initialize the game with the number of human and house_hagal players.
        board_type: base | rise_of_ix
        """
        self.difficulty = difficulty
        self.board_type = board_type
        self._check_players(n_human_players, n_house_hagal_players)
        self._check_difficulty(difficulty)
        self.colors = ["red", "blue", "green", "yellow"]
        self.n_human_players = n_human_players
        self.n_house_hagal_players = n_house_hagal_players
        self.turns_until_swordmaster = self._get_turns_until_swordmaster()
        self.players: List[Player] = []
        self.first_player = None
        self.players = self._get_players(
            n_human_players=self.n_human_players,
            n_house_hagal_players=self.n_house_hagal_players,
        )
        self.board = self._get_board()
        self.state = "started"
        self.turn_order = self._get_turn_order()
        self.first_player = self.turn_order[0]
        self.combat_deck = self._get_combat_deck()

    def start_new_round(self) -> None:
        """
        Start a new round.
        """
        self._round = RoundManager(
            board=self.board,
            combat_deck=self.combat_deck,
            first_player=self.first_player,
            turn_order=self.turn_order,
        )
        self._round.start_new_round()
        # self._round.take_player_turns()
        # self._round.resolve_combat()
        # self._round.update_makers()
        # self._round.recall_phase()
        # self.first_player = self._get_next_first_player(
        # current_first_player=self.first_player
        # )

    def _get_combat_deck(self) -> CombatDeck:
        """
        Return the combat deck.
        """
        return CombatDeck(self.board_type)

    def _get_next_first_player(self, current_first_player: Player) -> Player:
        """Get the next first player in the turn order."""
        if (
            self.turn_order.index(current_first_player)
            == len(self.turn_order) - 1
        ):
            return self.turn_order[0]
        return self.turn_order[self.turn_order.index(current_first_player) + 1]

    def _get_turn_order(self) -> List[Player]:
        """
        Return the turn order.
        """
        turn_order = self.players
        random.shuffle(turn_order)
        return turn_order

    def _check_difficulty(self, difficulty: str) -> None:
        """
        Check if the difficulty is valid.
        """
        if difficulty not in ["novice", "veteran", "expert"]:
            raise ValueError("Invalid difficulty.")

    def _check_players(
        self, n_human_players: int, n_house_hagal_players: int
    ) -> None:
        """
        Check if the number of players is between 2 and 4.
        """
        if n_human_players + n_house_hagal_players > 4:
            raise ValueError("Too many players. Max 4 players allowed.")

        if n_human_players + n_house_hagal_players < 2:
            raise ValueError("Too few players. Min 2 players allowed.")

    def _get_board(self) -> Board:
        """
        Return the board.
        """
        Board(board_type=self.board_type)

    def stop_game(self) -> None:
        """
        Stop the game.
        """
        self.state = "stopped"

    def _get_players(
        self, n_human_players: int, n_house_hagal_players: int
    ) -> List[Player]:
        """
        Return a list of all players in the game.
        """
        if self.players:
            return self.players

        players: List[Player] = []
        playable_leaders = self._get_human_leaders()
        players.extend(
            self._get_human_players(n_human_players, playable_leaders)
        )
        # update the playable leaders
        playable_leaders = self._get_house_hagal_leaders()
        # remove the leaders that are already taken by human players
        playable_leaders = self._update_playable_leaders(
            playable_leaders, players
        )
        players.extend(
            self._get_house_hagal_players(
                n_human_players, n_house_hagal_players, playable_leaders
            )
        )
        return players

    def _update_playable_leaders(
        self, playable_leaders: List[Leader], players: List[Player]
    ) -> List[Leader]:
        return [
            leader
            for leader in playable_leaders
            if leader.name not in [player.leader.name for player in players]
        ]

    def _get_leaders_from_config_file(self) -> list[dict]:
        with open("resources/dune_imperium.json", "r") as f:
            data = json.load(f)
            leaders: list[dict] = data["leaders"]

        if self.board_type == "rise_of_ix":
            with open("resources/rise_of_ix.json", "r") as f:
                data = json.load(f)
            leaders.extend(data["leaders"])

        return leaders

    def _get_human_leaders(self) -> List[Leader]:
        """
        Return a list of all human playable leaders.
        """
        leaders = self._get_leaders_from_config_file()
        return [Leader(**leader) for leader in leaders]

    def _get_house_hagal_leaders(self) -> List[Leader]:
        """
        Return a list of all house_hagal playable leaders.
        """
        leaders = self._get_leaders_from_config_file()

        return [
            Leader(**leader)
            for leader in leaders
            if leader.get("house_hagal_playable")
        ]

    def _get_human_players(
        self, n_human_players: int, playable_leaders: list[Leader]
    ) -> List[HumanPlayer]:
        """
        Return a list of human players, with randomly chosen leaders.
        """
        random.shuffle(playable_leaders)
        return [
            HumanPlayer(
                color=self.colors[i],
                player_id=i,
                leader=playable_leaders[i],
            )
            for i in range(n_human_players)
        ]

    def _get_turns_until_swordmaster(self) -> int:
        if self.difficulty == "novice":
            return 5
        elif self.difficulty == "veteran":
            return 4
        elif self.difficulty == "expert":
            return 3

    def _get_house_hagal_players(
        self,
        n_human_players: int,
        n_house_hagal_players: int,
        playable_leaders: List[Leader],
    ) -> List[HouseHagalPlayer]:
        """
        Return a list of house_hagal players, with randomly chosen leaders.
        """
        random.shuffle(playable_leaders)
        return [
            HouseHagalPlayer(
                color=self.colors[n_human_players + i],
                player_id=n_human_players + i,
                leader=playable_leaders[i],
                turns_until_swordmaster=self.turns_until_swordmaster,
            )
            for i in range(n_house_hagal_players)
        ]

    def get_winner(self) -> Player:
        """
        Return the player with the most points.
        """
        winner = self.players[0]
        for player in self.players:
            if player.points > winner.points:
                winner = player

        return winner

    def select_random_player(self) -> Player:
        """
        Return a random player.
        """
        return random.choice(self.players)
