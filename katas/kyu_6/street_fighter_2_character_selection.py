def street_fighter_selection(fighters, initial_position, moves):
    directions = {
        'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    max_x = len(fighters) - 1
    max_y = len(fighters[0])
    result = []
    x, y = initial_position
    for move in moves:
        move_x, move_y = directions[move]
        x = min(max(move_x + x, 0), max_x)
        y = (y + move_y) % max_y
        result.append(fighters[x][y])
    return result
