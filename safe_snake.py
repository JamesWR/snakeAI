import random
import json
from util.safe_moves import safe_moves
from util.snake_squares import snake_squares

directions = ['up', 'down', 'left', 'right']
def move(board):
    print('board', board)
    my_body = board.get('you').get('body')
    return { 'move': random.choice(safe_moves(snake_squares(board), my_body[0], x = board.get('board').get('width'), y = board.get('board').get('height'))) }
