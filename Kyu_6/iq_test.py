def iq_test(numbers):
    even = []
    odd = []
    for i, num in enumerate(map(int, numbers.split()), start=1):
        if num % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return min(even, odd, key=len)[0]
