grid = ['top left', 'top middle', 'top right',
        'middle left', 'center', 'middle right',
        'bottom left', 'bottom middle', 'bottom right']


def fire(x, y):
    return grid[x + y * 3]
