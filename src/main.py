from src.game.manager import Game

if __name__ == "__main__":

    # start the game
    game = Game(
        n_human_players=0,
        n_house_hagal_players=3,
        board_type="base",
        difficulty="novice",
    )

    print(game.first_player.color)
    game.start_new_round()
    # print(game.first_player.color)
    game.start_new_round()
    # print(game.first_player.color)
    # print(game.first_player.color)
