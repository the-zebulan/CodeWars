from collections import Counter


def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())

assert is_anagram('Creative', 'Reactive') is True
assert is_anagram('foefet', 'toffee') is True
assert is_anagram('Buckethead', 'DeathCubeK') is True
