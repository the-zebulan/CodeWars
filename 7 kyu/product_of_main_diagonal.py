from operator import mul


def main_diagonal_product(matrix):
    return reduce(mul, (matrix[a][a] for a in range(len(matrix))))

assert main_diagonal_product([[1,0],[0,1]]) == 1
assert main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) == 45
