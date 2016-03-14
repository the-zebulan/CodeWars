def reverse(string):
    return string if len(string) == 1 else string[-1] + reverse(string[:-1])
