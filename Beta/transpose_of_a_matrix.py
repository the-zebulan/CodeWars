def transpose(arr):
    return map(list, zip(*arr)) if all(arr) else [[]]


assert transpose([]) == []
assert transpose([[1]]) == [[1]]
assert transpose([[0, 1]]) == [[0], [1]]
assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
assert transpose([[]]) == [[]]
assert transpose([[], [], [], [], [], []]) == [[]]
