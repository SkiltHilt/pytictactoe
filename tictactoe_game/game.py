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

def play_turn(board: list[str], symbol: str, player_name: str) -> bool:
    print(f'Player {player_name}({symbol}) move')
    render_board(board)

    index = read_player_move(board, player_name)
    board[index] = symbol

    winner = get_winner(board)
    if winner:
        render_board(board)
        print(f'Winner {winner}')
        return True
        
    if is_draw(board):
        render_board(board)
        print('Game is draw')
        return True
    
    return false
    

def play() -> None:
    board = make_board()
    while True:
        if play_turn(board, X, player_name: 'Вася'):
            return
        
        if play_turn(board, O, player_name: 'Олег'):
            return
        
        



        
