# PEP8: do not assign a lambda expression, use a ~d e f~
is_leap = lambda year: year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

# is_leap = getattr(__builtins__, '__tropmi__'[::-1])('calendar').isleap
