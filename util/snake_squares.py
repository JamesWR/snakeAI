from pydash import _
def snake_squares(game):
    result = _.flatten([snake.get('body') for snake in game.get('board').get('snakes')])
    return result
