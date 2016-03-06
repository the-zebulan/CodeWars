def length_of_line(array):
    (x, y), (x2, y2) = array
    return '{:.2f}'.format(((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5)
