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
