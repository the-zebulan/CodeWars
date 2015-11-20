def fizzbuzz(n):
    if not n % 15:
        return 'fizz buzz'
    elif not n % 3:
        return 'fizz'
    elif not n % 5:
        return 'buzz'
    return n


# def fizzbuzz(n):
#     result = []
#     if not n % 3:
#         result.append('fizz')
#     if not n % 5:
#         result.append('buzz')
#     return ' '.join(result) if result else n


assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == "fizz"
assert fizzbuzz(4) == 4
assert fizzbuzz(9) == "fizz"
assert fizzbuzz(15) == "fizz buzz"
assert fizzbuzz(20) == "buzz"
assert fizzbuzz(25) == "buzz"
assert fizzbuzz(37) == 37
assert fizzbuzz(45) == "fizz buzz"
