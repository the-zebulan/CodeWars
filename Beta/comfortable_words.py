LEFT = set('qwertasdfgzxcvb')
RIGHT = set('yuiophjklnm')


def comfortable_word(word):
    one = []
    two = []
    for i, a in enumerate(word):
        if not i % 2:
            one.append(a)
        else:
            two.append(a)
    one = ''.join(one)
    two = ''.join(two)
    return LEFT.issuperset(one) and RIGHT.issuperset(two) or \
        LEFT.issuperset(two) and RIGHT.issuperset(one)


assert comfortable_word('yams') is True
assert comfortable_word('test') is False
