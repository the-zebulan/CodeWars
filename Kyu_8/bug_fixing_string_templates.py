def build_string(*args):
    return "I like {}!".format(", ".join(args))

assert build_string('Cheese', 'Milk', 'Chocolate') == \
    'I like Cheese, Milk, Chocolate!'
assert build_string('Cheese', 'Milk') == 'I like Cheese, Milk!'
assert build_string('Chocolate') == 'I like Chocolate!'
