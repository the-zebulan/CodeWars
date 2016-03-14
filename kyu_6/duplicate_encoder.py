from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    cnt = Counter(word)
    return ''.join('(' if cnt[a] == 1 else ')' for a in word)
