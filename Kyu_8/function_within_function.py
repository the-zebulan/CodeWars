# def always(n=0):
#     def closure():
#         return n
#     return closure


def always(n=0):
    return lambda: n
