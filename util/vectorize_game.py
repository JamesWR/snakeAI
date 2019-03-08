from enum import Enum
from pydash import _
import json
from util.print_board import print_board

class Point(Enum):
    EMPTY = 0
    OFF_BOARD = 1
    SNAKE_BODY = 2
    SNAKE_TAIL = 3
    SNAKE_HEAD = 4
    FOOD = 5
_view_size_ = 21


def vectorize(game):
    head_point = game.get('you').get('body')[0]
    height = game.get('board').get('height')
    width = game.get('board').get('width')
    left_overflow = int(max(((_view_size_ - 1) / 2) - head_point.get('x'), 0))
    right_overflow =  int(max(
        (head_point.get('x') + ((_view_size_ - 1) / 2) - width), 
        0
    ))
    up_overflow = int(max(((_view_size_ - 1) / 2) - head_point.get('y'), 0))
    down_overflow =  int(max(
        (head_point.get('x') + ((_view_size_ - 1) / 2) - width), 
        0
    ))
    start = ([[Point.OFF_BOARD] * _view_size_] * up_overflow)
    middle = ([
        ([Point.OFF_BOARD] * left_overflow) + \
        ([Point.EMPTY] * (_view_size_ - left_overflow - right_overflow)) + \
        ([Point.OFF_BOARD] * right_overflow)
    ] * _view_size_)
    end = ([[Point.OFF_BOARD] * _view_size_] * down_overflow)
    board = start + middle + end
    for food in game.get('board').get('food'):
        board[food.get('x')][food.get('y')] = Point.FOOD

    return board

def test(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print_board(vectorize(data))