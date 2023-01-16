from src.game.players.player import Player
from src.game.board.board import Board


class Game:
    def __init__(self, n_players: int):
        if n_players > 4:
            raise ValueError("Too many players. Max 4 players")
        if n_players < 2:
            raise ValueError("Too few players. Min 2 players")
        self.n_players = n_players
        self.state = "initializing"
        self.initialize_game()

    def initialize_game(self):
        self.players = self.get_players(self.n_players)
        self.board = Board()
        self.state = "started"

    def stop_game(self):
        self.state = "stopped"

    def get_players(self, n_players: int):
        colors = ["red", "blue", "green", "yellow"]
        return [Player(colors[i]) for i in range(n_players)]

    def get_winner(self):
        # find the player with the most points
        winner = self.players[0]
        for player in self.players:
            if player.points > winner.points:
                winner = player

        return winner
