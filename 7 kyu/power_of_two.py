def power_of_two(num):
    return bin(num).count('1') == 1

assert power_of_two(1) is True
assert power_of_two(2) is True
assert power_of_two(5) is False
assert power_of_two(4096) is True
assert power_of_two(33554432) is True
assert power_of_two(8388608) is True
assert power_of_two(16777216) is True
assert power_of_two(8388608) is True
assert power_of_two(4194304) is True
assert power_of_two(4194305) is False
assert power_of_two(16777217) is False
assert power_of_two(16777215) is False
