import random
from typing import List
import json

from src.game.board.board import Board
from src.game.leaders.leader import Leader
from src.game.players.house_hagal import HouseHagalPlayer
from src.game.players.human import HumanPlayer
from src.game.players.player import Player


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
        """Initialize the game with the number of human and house_hagal players."""
        self.difficulty = difficulty
        self.board_type = board_type
        self._check_players(n_human_players, n_house_hagal_players)
        self._check_difficulty(difficulty)
        self.colors = ["red", "blue", "green", "yellow"]
        self.n_human_players = n_human_players
        self.n_house_hagal_players = n_house_hagal_players
        self.state = "initializing"
        self.players: List[Player] = []
        self.first_player = None
        self._initialize_game()

    def _check_difficulty(self, difficulty: str):
        """
        Check if the difficulty is valid.
        """
        if difficulty not in ["novice", "veteran", "expert"]:
            raise ValueError("Invalid difficulty.")

    def _check_players(self, n_human_players: int, n_house_hagal_players: int):
        """
        Check if the number of players is between 2 and 4.
        """
        if n_human_players + n_house_hagal_players > 4:
            raise ValueError("Too many players. Max 4 players allowed.")

        if n_human_players + n_house_hagal_players < 2:
            raise ValueError("Too few players. Min 2 players allowed.")

    def _initialize_game(self):
        """
        Initialize the game state, players and board.
        """
        self.players = self._get_players(
            n_human_players=self.n_human_players,
            n_house_hagal_players=self.n_house_hagal_players,
        )
        self.first_player = self._decide_first_player()
        self.board = self._get_board()
        self.state = "started"

    def _get_board(self) -> Board:
        """
        Return the board.
        """
        Board(board_type=self.board_type)

    def stop_game(self):
        """
        Stop the game.
        """
        self.state = "stopped"

    def _get_players(self, n_human_players: int, n_house_hagal_players: int):
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
    ):
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
    ) -> list:
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

    def _get_house_hagal_players(
        self,
        n_human_players: int,
        n_house_hagal_players: int,
        playable_leaders: List[Leader],
    ) -> list:
        """
        Return a list of house_hagal players, with randomly chosen leaders.
        """
        random.shuffle(playable_leaders)
        return [
            HouseHagalPlayer(
                color=self.colors[n_human_players + i],
                player_id=n_human_players + i,
                leader=playable_leaders[i],
            )
            for i in range(n_house_hagal_players)
        ]

    def get_winner(self):
        """
        Return the player with the most points.
        """
        winner = self.players[0]
        for player in self.players:
            if player.points > winner.points:
                winner = player

        return winner

    def _decide_first_player(self):
        """
        Decide which player starts the game, randomly.
        """
        self.first_player = random.choice(self.players)
