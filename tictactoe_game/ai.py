from random import choice
from tictactoe_game.rules import available_moves

def pick_ai_move(board: list[str]) -> int:
    moves = available_moves(board)
    return choice(moves)