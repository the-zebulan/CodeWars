def solution(string, ending):
    return string.endswith(ending)

assert solution('abc', 'bc') is True
assert solution('abc', 'd') is False
