from models.model import Board, Game, Player
from src.constants import PLAYER1_NAME, PLAYER2_NAME
import requests
import json


def main():

    Players = (
        Player(name=PLAYER1_NAME),
        Player(name=PLAYER2_NAME),
    )
    game = Game(players=Players)
    board = Board(game)

    while True:
        responseX = requests.get(
            "http://127.0.0.1:5001/random/default/choice?value=0&value=1&value=2",
            timeout=5,
        )
        responseY = requests.get(
            "http://127.0.0.1:5001/random/default/choice?value=0&value=1&value=2",
            timeout=5,
        )
        responseX = int(json.loads(responseX.text)["value"])
        responseY = int(json.loads(responseY.text)["value"])
        board.play(responseX, responseY)


if __name__ == "__main__":
    main()
