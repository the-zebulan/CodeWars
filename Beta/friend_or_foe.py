def friend(x):
    return [a for a in x if len(a) == 4]

assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
