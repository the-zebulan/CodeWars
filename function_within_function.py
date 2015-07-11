def always(n=0):
    def closure():
        return n
    return closure

three = always(3)
assert three() == 3
