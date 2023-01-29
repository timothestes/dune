from src.game.players.player import Player
from unittest.mock import Mock


def test_player_init():
    leader = Mock()
    leader.name = "leader"
    player = Player(color="red", leader=leader)
    assert player.player_id is not None
    assert player.leader.name == "leader"
    assert player.hand == []
    assert player.points == 0
    assert player.color == "red"
    assert player.resources.water == 1
    assert player.resources.spice == 0
    assert player.resources.solari == 0
    assert player.influence.emperor == 0
    assert player.influence.spacing_guild == 0
    assert player.influence.bene_gesserit == 0
    assert player.influence.fremen == 0
    assert player.garrison.n_troops_in_garrison == 3
    assert player.agents[0].color == "red"
    assert player.agents[1].color == "red"
    assert player.get_combat_points() == 0
    assert player.play_combat_cards() == "TODO"
