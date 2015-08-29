def average(x):
    return sum(x) / len(x) if not isinstance(x, str) else 'Incorrect'

assert average("Hello please let me break your program") == "Incorrect"
assert average([70, 70]) == 70
assert average([40, 20, 5]) == 21
