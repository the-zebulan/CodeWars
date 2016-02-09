def boolean_to_string(b):
    return ('False', 'True')[b]


assert boolean_to_string(True) == 'True'
assert boolean_to_string(False) == 'False'
