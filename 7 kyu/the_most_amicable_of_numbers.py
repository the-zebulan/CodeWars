def proper_divisors_sum(n):
    return sum(a for a in xrange(1, n) if not n % a)


def amicable_numbers(a, b):
    return proper_divisors_sum(a) == b and proper_divisors_sum(b) == a


assert amicable_numbers(220, 284) is True
assert amicable_numbers(220, 280) is False
assert amicable_numbers(1184, 1210) is True
assert amicable_numbers(220221, 282224) is False
assert amicable_numbers(10744, 10856) is True
assert amicable_numbers(299920, 9284) is False
assert amicable_numbers(999220, 2849) is False
assert amicable_numbers(122265, 139815) is True
assert amicable_numbers(220, 284) is True
assert amicable_numbers(220, 284) is True
