from operator import mul


def main_diagonal_product(matrix):
    return reduce(mul, (matrix[a][a] for a in xrange(len(matrix))))
