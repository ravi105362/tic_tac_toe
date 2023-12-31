from src.models.model import Player, Position, Board, Game
from src.constants import SIZE

# TODO Add exhaustive unit tests


def test_player():
    player_obj = Player("test player one")
    assert player_obj.name == "test player one"


def test_move():
    move_obj = Position(1, 1, "Test player two")
    assert move_obj.row == 1
    assert move_obj.col == 1
    assert move_obj.name == "Test player two"


def test_game_constructor():
    player_obj_1 = Player("test player one")
    player_obj_2 = Player("test player two")
    game_obj = Game(players=[player_obj_1, player_obj_2])
    assert game_obj.size == SIZE
    assert game_obj.current_player == player_obj_1


def test_board_constructor():
    player_obj_1 = Player("test player one")
    player_obj_2 = Player("test player two")
    game_obj = Game(players=[player_obj_1, player_obj_2])
    board_obj = Board(game_obj)
    assert board_obj._game == game_obj
