from src.game.board.board import Board
from src.game.players.house_hagal import HouseHagalPlayer
from src.game.players.human import HumanPlayer


class Game:
    def __init__(self, n_human_players: int, n_house_hagal_players: int = 0):
        self._check_players(n_human_players, n_house_hagal_players)
        self.colors = ["red", "blue", "green", "yellow"]
        self.n_human_players = n_human_players
        self.n_house_hagal_players = n_house_hagal_players
        self.state = "initializing"
        self.initialize_game()

    def _check_players(self, n_human_players: int, n_house_hagal_players: int):
        if n_human_players + n_house_hagal_players > 4:
            raise ValueError("Too many players. Max 4 players allowed.")

        if n_human_players + n_house_hagal_players < 2:
            raise ValueError("Too few players. Min 2 players allowed.")

    def initialize_game(self):
        self.players = self._get_players(
            n_human_players=self.n_human_players,
            n_house_hagal_players=self.n_house_hagal_players,
        )
        self.board = Board()
        self.state = "started"

    def stop_game(self):
        self.state = "stopped"

    def _get_players(self, n_human_players: int, n_house_hagal_players: int):
        players = []
        players.extend(self._get_human_players(n_human_players))
        players.extend(
            self._get_house_hagal_players(
                n_human_players, n_house_hagal_players
            )
        )
        return players

    def _get_human_players(self, n_human_players: int) -> list:
        return [
            HumanPlayer(color=self.colors[i], player_id=i)
            for i in range(n_human_players)
        ]

    def _get_house_hagal_players(
        self, n_human_players: int, n_house_hagal_players: int
    ) -> list:
        return [
            HouseHagalPlayer(
                color=self.colors[i + n_human_players],
                player_id=i + n_human_players,
            )
            for i in range(n_house_hagal_players)
        ]

    def get_winner(self):
        # find the player with the most points
        winner = self.players[0]
        for player in self.players:
            if player.points > winner.points:
                winner = player

        return winner
