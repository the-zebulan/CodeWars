def chained(functions):
    return lambda a: reduce(lambda arg, func: func(arg), functions, a)

    # def inner(arg):
    #     result = arg
    #     for func in functions:
    #         result = func(result)
    #     return result
    # return inner
