def get_score(n):
    return n * (n + 1) * 25


assert get_score(1) == 50
assert get_score(2) == 150
assert get_score(3) == 300
assert get_score(4) == 500
assert get_score(5) == 750
