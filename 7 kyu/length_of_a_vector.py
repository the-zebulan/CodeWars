def vector_length(vector):
    (x, y), (x2, y2) = vector
    return ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5

assert vector_length([[0, 1],[0, 0]]) ==  1
assert vector_length([[0, 3],[4, 0]]) == 5
assert vector_length([[1, -1],[1, -1]]) == 0
