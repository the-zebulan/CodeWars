grid = ['top left', 'top middle', 'top right',
        'middle left', 'center', 'middle right',
        'bottom left', 'bottom middle', 'bottom right']


def fire(x, y):
    return grid[x + y * 3]

assert fire(0, 0) == 'top left'
assert fire(1, 2) == 'bottom middle'
assert fire(1, 1) == 'center'
