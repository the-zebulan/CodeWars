def iq_test(numbers):
    even = []
    odd = []
    for i, num in enumerate(map(int, numbers.split()), start=1):
        if num % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return min(even, odd, key=len)[0]

assert iq_test('2 4 7 8 10') == 3
assert iq_test('1 2 1 1') == 2
assert iq_test('1 2 2') == 1
