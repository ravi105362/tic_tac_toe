from src.models.model import Player, Move, Board, Game


def test_player():
    player_obj = Player("test player one")
    assert player_obj.name == "test player one"


def test_move():
    move_obj = Move(1, 1, "Test player two")
    assert move_obj.row == 1
    assert move_obj.col == 1
    assert move_obj.name == "Test player two"
