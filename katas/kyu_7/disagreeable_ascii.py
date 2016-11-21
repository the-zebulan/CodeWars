def get_weight(name):
    return sum(ord(a) for a in name.swapcase() if a.isalpha())


# Kata function name should use snake_case not mixedCase
getWeight = get_weight
