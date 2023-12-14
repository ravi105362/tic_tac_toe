from enum import Enum
from dataclasses import dataclass
from itertools import cycle
from src.constants import BOARD_SIZE, PLAYER1_NAME, PLAYER2_NAME
import sys

# TODO Add logging instead of print statements


@dataclass
class Player:
    """Used to store Player information"""

    name: str


@dataclass
class Move:
    """Used to store Move information"""

    row: int
    col: int
    name: str = ""


class Board:
    """Used to store the board data"""

    def __init__(self, game):
        self._cells = {}
        self._game = game

    def play(self, row, col):
        move = Move(row, col, self._game.current_player.name)
        if self._game.check_valid_move(move):
            self._game.process_move(move)
            for row_state in range(len(self._game._current_moves)):
                for col_state in range(len(self._game._current_moves[0])):
                    print(self._game._current_moves[row_state][col_state], end="\t")
                print()
            if self._game.is_tied():
                print("****Game Tied****")
                sys.exit(0)
            elif self._game.has_winner():
                msg = f'****Player "{self._game.current_player.name}" won!****'
                print(msg)
                sys.exit(0)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.name}'s turn"
                print(msg)

    def reset_board(self):
        self._game.reset_game()


class Game:
    """Used to store the game data"""

    def __init__(self, players, board_size=BOARD_SIZE):
        self.board_size = board_size
        self._players = cycle(players)
        self.current_player = next(self._players)
        self._current_moves = []
        self._has_winner = False
        self._winning_possibilities = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_possibilities = self._get_winning_possibilities()

    def _get_winning_possibilities(self):
        rows = [[(move.row, move.col) for move in row] for row in self._current_moves]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def toggle_player(self):
        self.current_player = next(self._players)

    def check_valid_move(self, move):
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].name == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_possibilities:
            results = set(self._current_moves[n][m].name for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                break

    def has_winner(self):
        return self._has_winner

    def is_tied(self):
        no_winner = not self._has_winner
        played_moves = [move.name for row in self._current_moves for move in row]
        return no_winner and all(played_moves)

    def reset_game(self):
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []
