def dir_reduc(directions):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST',
                'SOUTH': 'NORTH', 'WEST': 'EAST'}
    result = []
    for direction in directions:
        if result and result[-1] == opposite[direction]:
            result.pop()
        else:
            result.append(direction)
    return result


# PEP8: Kata function name should use snake_case
dirReduc = dir_reduc
