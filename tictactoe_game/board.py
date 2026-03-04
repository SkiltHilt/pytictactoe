from tictactoe_game.constants import BOARD_SIZE, UNIT, EMPTY

def make_board() -> list[str]:
    return [EMPTY] * BOARD_SIZE

def render_board(board: list[str]) -> None:
    def cell(i: int) -> str:
        return str(i + 1) if board[i] == EMPTY else board[i]
    line = UNIT * 3 + '+'
    print(line)
    for row in range(3):
        print(f'| {cell(row * 3)} | {cell(row * 3 + 1)} | {cell(row * 3 + 2)} |')
        print(line)


# [' ',' ',' ',' ',' ',' ',' ',' ',' ']