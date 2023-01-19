from src.game.manager import Game

if __name__ == "__main__":

    # start the game
    game = Game(
        n_human_players=0,
        n_house_hagal_players=3,
        board_type="rise_of_ix",
        difficulty="novice",
    )

    game._decide_first_player()

    # for player in game.players:
    # print(player)
