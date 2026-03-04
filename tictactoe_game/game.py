from tictactoe_game.constants import EMPTY

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