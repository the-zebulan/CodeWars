# def count_sheeps(sheeps):
#     return sum(sheep for sheep in sheeps if sheep is not None)


def count_sheeps(sheeps):
    return sheeps.count(True)

assert count_sheeps([True, True, True, False,
                     True, True, True, True,
                     True, False, True, False,
                     True, False, False, True,
                     True, True, True, True,
                     False, False, True, True]) == 17
