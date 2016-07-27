def SumSquares(lst):
    """ sum_squares == PEP8 (forced PascalCase by Codewars) """
    try:
        return sum(SumSquares(a) for a in lst)
    except TypeError:
        return lst ** 2
