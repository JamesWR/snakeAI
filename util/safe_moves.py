
all_valid = ['up', 'left', 'down', 'right']

def safe_moves(fill_squares, current_square, x = 10, y = 10):
    result = all_valid.copy()
    print('safe moves in: ', current_square, x, y, fill_squares)
    left = {'x': current_square.get('x') - 1, 'y': current_square.get('y')}
    right = {'x': current_square.get('x') + 1, 'y': current_square.get('y')}
    down = {'x': current_square.get('x'), 'y': current_square.get('y') + 1}
    up = {'x': current_square.get('x'), 'y': current_square.get('y') - 1}
    if(left in fill_squares or left.get('x') < 0):
        print('left:', left in fill_squares, left.get('x') < 0)
        result.remove('left')
    if(right in fill_squares or right.get('x') >= x):
        print('right:', right in fill_squares, right.get('x') >= x)
        result.remove('right')
    if(down in fill_squares or down.get('y') >= y):
        print('down:', down in fill_squares, down.get('y') >= y)
        result.remove('down')
    if(up in fill_squares or up.get('y') < 0):
        print('up:', up in fill_squares, up.get('y') < 0)
        result.remove('up')
    if(len(result) == 0):
        result = ['down']
    print('safe moves', result)
    return result
