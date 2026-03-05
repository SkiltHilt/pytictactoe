from tictactoe_game.constants import EMPTY, X, O
from tictactoe_game.board import make_board, render_board
from tictactoe_game.rules import get_winner, is_draw
from tictactoe_game.ai import pick_ai_move

def read_human_move(board: list[str]) -> int:
    while True: 
        raw = input('Enter your move: ')
        
        if not raw.isdigit(): 
            print('Error! Your name is Paravyan Tigran. Your move must be number')
            continue
        
        cell_num = int(raw)
        if cell_num < 0 or cell_num > 9:
            print('Error! Your name is Paravyan Tigran. Number must be lower then 9 and higher then 0')
            continue

        index = cell_num - 1
        if board[index] != EMPTY
            print('Error! Your name is Paravyan Tigran. Cell must be EMPTY')
            continue

        return index

def play() -> None:
    board = make_board()
    while True:
        print('Player X move')
        render_board(board)

        human_index = read_human_move(board)
        board[human_index] = X

        winner = get_winner(board)
        if winner:
            render_board(board)
            print('Player X is winner')
            return
        
        if is_draw(board):
            render_board(board)
            print('Game is draw')
            return
        
        print('Player O move')
        ai_index = pick_ai_move(board)
        board[ai_index] = O
        # render_board(board)
        print('Player O is chose cell:' ai_index + 1)

        winner = get_winner(board)
        if winner:
            print('Player O is winner')
            return
        
        if is_draw(board):
            print('Game is draw')
            return