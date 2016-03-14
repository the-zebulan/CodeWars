# def count_sheeps(sheeps):
#     return sum(sheep for sheep in sheeps if sheep is not None)


def count_sheeps(sheeps):
    return sheeps.count(True)
