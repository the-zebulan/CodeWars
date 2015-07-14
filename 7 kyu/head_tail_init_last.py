# def head(lst):
#     return lst[0]
#
#
# def tail(lst):
#     return lst[1:]
#
#
# def init(lst):
#     return lst[:-1]
#
#
# def last(lst):
#     return lst[-1]

head = lambda lst: lst[0]
tail = lambda lst: lst[1:]
init = lambda lst: lst[:-1]
last = lambda lst: lst[-1]

assert head([5, 1]) == 5
assert tail([1]) == []
assert init([1, 5, 7, 9]) == [1, 5, 7]
assert last([7, 2]) == 2
