def my_first_kata(a, b):
    try:
        if not (isinstance(a, bool) or isinstance(b, bool)):
            return a % b + b % a
    except (TypeError, ZeroDivisionError):
        pass
    return False
