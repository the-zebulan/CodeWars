from itertools import cycle


def snail(arr):
    if arr == [[]]:
        return []
    direction = cycle('RDLU')
    x_top = y_left = 0
    x_bottom = y_right = len(arr) - 1
    total_elements = len(arr) ** 2
    result = []
    while len(result) < total_elements:
        current_direction = next(direction)
        if current_direction == 'R':
            result.extend(arr[x_top][a] for a in xrange(y_left, y_right + 1))
            x_top += 1
        elif current_direction == 'D':
            result.extend(
                arr[b][y_right] for b in xrange(x_top, x_bottom + 1))
            y_right -= 1
        elif current_direction == 'L':
            result.extend(
                arr[x_bottom][c] for c in xrange(y_right, y_left - 1, -1))
            x_bottom -= 1
        elif current_direction == 'U':
            result.extend(
                arr[d][y_left] for d in xrange(x_bottom, x_top - 1, -1))
            y_left += 1
    return result
