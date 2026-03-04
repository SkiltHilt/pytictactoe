from tictactoe_game.board import make_board, render_board
from tictactoe_game.game import read_human_move

board = make_board
render_board(board)

index = read_human_move(board)

print(index)