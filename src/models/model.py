from enum import Enum
from dataclasses import dataclass, field
from itertools import cycle
from src.constants import SIZE, PLAYER1_NAME, PLAYER2_NAME
import sys
from typing import Any
import numpy as np
from src.utils import get_column_wise, get_diagonal_main, get_diagonal_second

# TODO Add logging instead of print statements


@dataclass
class Player:
    """Used to store Player information"""

    name: str


@dataclass
class Position:
    """Used to store details at a position"""

    row: int
    col: int
    name: str = ""


@dataclass
class Game:
    """Used to store the game data"""

    players: Any
    size: int = 3
    _moves: list = field(default_factory=list)
    _winner_found = False
    _winning_possibilities: list = field(default_factory=list)

    def __post_init__(self):
        self._players = cycle(self.players)
        self.current_player = next(self._players)
        self._moves = [
            [Position(row, col) for col in range(self.size)] for row in range(self.size)
        ]
        self._winning_possibilities = self._get_winning_possibilities()

    def _get_winning_possibilities(self):
        rows = [
            [(position.row, position.col) for position in row] for row in self._moves
        ]
        return (
            rows
            + get_column_wise(rows)
            + [get_diagonal_main(rows), get_diagonal_second(rows)]
        )

    def valid_check(self, position):
        row, col = position.row, position.col
        not_used = self._moves[row][col].name == ""
        no_winner = not self._winner_found
        return no_winner and not_used

    def insert(self, position):
        row, col = position.row, position.col
        self._moves[row][col] = position
        for combo in self._winning_possibilities:
            results = {self._moves[n][m].name for n, m in combo}
            if len(results) == 1 and "" not in results:
                self._winner_found = True
                break

    def is_tied(self):
        no_winner = not self._winner_found
        played_moves = [position.name for row in self._moves for position in row]
        return no_winner and all(played_moves)


@dataclass
class Board:
    """Used to store the board data"""

    _game: Game

    def play(self, row, col):
        position = Position(row, col, self._game.current_player.name)
        if self._game.valid_check(position):
            self._game.insert(position)
            for row_state in range(len(self._game._moves)):
                for col_state in range(len(self._game._moves[0])):
                    print(self._game._moves[row_state][col_state], end="\t")
                print()
            print("Next Move")
            if self._game._winner_found:
                msg = f'****Player "{self._game.current_player.name}" won!****'
                print(msg)
                sys.exit(0)
            elif self._game.is_tied():
                print("****Game Tied****")
                sys.exit(0)
            else:
                self._game.current_player = next(self._game._players)
