def manhattan_distance(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2)


def logistic_map(width, height, x_list, y_list):
    matrix = [[None for __ in range(width)] for _ in range(height)]
    if not x_list or not y_list:
        return matrix
    supply_points = set(zip(y_list, x_list))
    for r, row in enumerate(matrix):
        for c, col_item in enumerate(row):
            if col_item != 0:
                matrix[r][c] = min(
                    manhattan_distance(r, c, x2, y2)
                    for x2, y2 in supply_points
                )
    return matrix
