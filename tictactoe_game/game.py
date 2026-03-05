from tictactoe_game.constants import EMPTY, X, O
from tictactoe_game.board import make_board, render_board
from tictactoe_game.rules import get_winner, is_draw
# from tictactoe_game.ai import pick_ai_move

def read_player_move(board: list[str], palyer_name: str) -> int:
    while True: 
        raw = input(f'{palyer_name} Enter your move ( 1 - 9 ): ')
        
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

        index_1 = read_player_move(board, player_name: 'Вася')
        board[index_1] = X

        winner = get_winner(board)
        if winner:
            render_board(board)
            print(f'Winner {winner}')
            return
        
        if is_draw(board):
            render_board(board)
            print('Game is draw')
            return
        
        print('Player O move')
        render_board(board)
        index_2 = read_player_move(board, player_name: 'Олег')
        board[index_2] = O

        winner = get_winner(board)
        if winner:
            render_board(board)
            print(f'Winner {winner}')
            return
        
        if is_draw(board):
            render_board(board)
            print('Game is draw')
            return