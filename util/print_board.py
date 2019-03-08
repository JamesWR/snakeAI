from pydash import _
def print_board(board):
    for row in board:
        print(*(_.map_(row, lambda x: x.value)))
             