def caffeineBuzz(n):
    if n % 12 == 0:
        return 'CoffeeScript'
    elif n % 6 == 0:
        return 'JavaScript'
    elif n % 3 == 0:
        return 'Java'
    return 'mocha_missing!'
