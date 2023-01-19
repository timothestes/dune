from typing import List

from src.game.board.board import Board
from src.game.players.house_hagal import HouseHagalPlayer
from src.game.players.human import HumanPlayer
from src.game.players.player import Player


class Game:
    """
    A class representing a game.
    """

    def __init__(self, n_human_players: int, n_house_hagal_players: int = 0):
        """Initialize the game with the number of human and house_hagal players."""
        self._check_players(n_human_players, n_house_hagal_players)
        self.colors = ["red", "blue", "green", "yellow"]
        self.n_human_players = n_human_players
        self.n_house_hagal_players = n_house_hagal_players
        self.state = "initializing"
        self.players: List[Player] = []
        self._initialize_game()

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
        self.board = Board()
        self.state = "started"

    def stop_game(self):
        """
        Stop the game.
        """
        self.state = "stopped"

    def _get_players(self, n_human_players: int, n_house_hagal_players: int):
        """
        Return a list of all players in the game.
        """
        players = []
        players.extend(self._get_human_players(n_human_players))
        players.extend(
            self._get_house_hagal_players(
                n_human_players, n_house_hagal_players
            )
        )
        return players

    def _get_human_players(self, n_human_players: int) -> list:
        """
        Return a list of human players.
        """
        return [
            HumanPlayer(color=self.colors[i], player_id=i)
            for i in range(n_human_players)
        ]

    def _get_house_hagal_players(
        self, n_human_players: int, n_house_hagal_players: int
    ) -> list:
        """
        Return a list of house_hagal players.
        """
        return [
            HouseHagalPlayer(
                color=self.colors[i + n_human_players],
                player_id=i + n_human_players,
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
