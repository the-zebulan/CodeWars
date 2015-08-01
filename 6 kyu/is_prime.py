def is_prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    return True

assert is_prime(0) is False
assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(4) is False
