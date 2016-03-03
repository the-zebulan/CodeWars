def my_first_kata(a, b):
    try:
        if not (isinstance(a, bool) or isinstance(b, bool)):
            return a % b + b % a
    except (TypeError, ZeroDivisionError):
        pass
    return False


assert my_first_kata(10, False) is False
assert my_first_kata(3, 5) == (3 % 5 + 5 % 3)
assert my_first_kata("hello", 3) is False
assert my_first_kata(67, "bye") is False
assert my_first_kata(True, True) is False
assert my_first_kata(314, 107) == (107 % 314 + 314 % 107)
assert my_first_kata(1, 32) == (1 % 32 + 32 % 1)
assert my_first_kata(-1, -1) == (-1 % -1 + -1 % -1)
assert my_first_kata(19483, 9) == (9 % 19483 + 19483 % 9)
assert my_first_kata("hello", {}) is False
assert my_first_kata([], "pippi") is False
