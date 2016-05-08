# Section 1: "lambda" <-- PEP8: do not assign a lambda expression, use def
a_simple_function = lambda a, b, (c, d), e=True, *r, **k: "I'm simple enough!"

# Section 2: "list comprehension"
my_list = ['A' * i for i in xrange(10) if i != 5]

# Section 3: "dictionary comprehension"
lowercase_to_uppercase = {i: i.upper() for i in 'abcdefghijklmnopqrstuvwxyz'}

# Section 4: "__import__"
path = __import__('os.path', fromlist=['join']).join('/', 'usr', 'bin')

# Section 5: "ternary operator"
a = 42  # if True else -1
