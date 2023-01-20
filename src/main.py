from src.game.manager import Game

if __name__ == "__main__":

    # start the game
    game = Game(
        n_human_players=0,
        n_house_hagal_players=3,
        board_type="base",
        difficulty="novice",
    )

    for player in game.players:
        print(player.agents[1].color)
