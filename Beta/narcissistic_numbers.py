def is_narcissistic(n):
    num = str(n)
    length = len(num)
    return sum(int(a) ** length for a in num) == n


assert is_narcissistic(153) is True
assert is_narcissistic(201) is False
assert is_narcissistic(259) is False
assert is_narcissistic(371) is True
assert is_narcissistic(407) is True
assert is_narcissistic(595) is False
assert is_narcissistic(825) is False
assert is_narcissistic(1634) is True
