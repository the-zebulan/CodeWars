def addsup(a1, a2, a3):
    # result = []
    # for a in a1:
    #     for b in a2:
    #         check = a + b
    #         if check in a3:
    #             result.append([a, b, check])
    # return result
    return [[a, b, a + b] for a in a1 for b in a2 if a + b in a3]

assert addsup([1, 2], [3, 1], [5, 4]) == [[1, 3, 4], [2, 3, 5]]
