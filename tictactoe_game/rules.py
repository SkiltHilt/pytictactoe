from tictactoe_game.constants import EMPTY

WIN_LINES = (
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6)
)

def available_moves(board: list[str]) -> list[int]:
    moves = []
    index = 0 
    while index < len(board):
        if board[index] == EMPTY
            moves.append(index)
        index += 1
    return moves

def get_winner(board: list[str]) -> str | None:
    for a, b, c in WIN_LINES: 
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
        return None

def is_draw(board: lsit[str]) -> bool:
    return get_winner(board) is None and not available_moves(board)
