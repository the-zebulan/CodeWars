def logical_matrix(matrix):
    return all(item in (0, 1) for row in matrix for item in row)


def nonnegative_matrix(matrix):
    return all(item >= 0 for row in matrix for item in row)


def sum_nonnegative_logical_matrix(matrix1, matrix2):
    if logical_matrix(matrix1) and nonnegative_matrix(matrix1) and \
            logical_matrix(matrix2) and nonnegative_matrix(matrix2):
        return sum(sum(c for b in a for c in b) for a in (matrix1, matrix2))
    return False


assert logical_matrix([[0, 0], [1, 1]]) is True
assert logical_matrix([[2, 7], [0, 0]]) is False
assert logical_matrix([[1, 1], [1, 2]]) is False
assert nonnegative_matrix([[0, 0], [1, 1]]) is True
assert nonnegative_matrix([[0, 0, 0, 0], [1, 1, 0, 1]]) is True
assert sum_nonnegative_logical_matrix([[0, 0, 1], [1, 1, 0], [0, 0, 0]],
                                      [[0, 0, 1], [1, 1, 0], [0, 0, 0]]) == 6


# # merged all three functions below
# def hmm(*args):
#     is_logical = is_positive = True
#     total = 0
#     for matrix in args:
#         for row in matrix:
#             for item in row:
#                 # if not 0 <= item <= 1:
#                 if not item in (0, 1):
#                     is_logical = False
#                 if item < 0:
#                     is_positive = False
#                 total += item
#     if is_logical and is_positive:
#         return total
#     return False
# assert hmm([[0, 0, 1], [1, 1, 0], [0, 0, 0]],
#            [[0, 0, 1], [1, 1, 0], [0, 0, 0]]) == 6
