def snail(arr):
    """ Inspired by a solution on Codewars by MMMAAANNN """
    matrix = list(arr)
    result = []
    while matrix:
        result.extend(matrix.pop(0))
        matrix = zip(*matrix)
        matrix.reverse()
    return result
